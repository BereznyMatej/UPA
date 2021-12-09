from typing import List
import pandas as pd
import argparse

from dataset import Dataset

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query_list', nargs='+', required=True, type=str)
    return parser.parse_args()
    

class Query:

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.loaded_dfs = {}


    def __load_dfs(self, df_name_list) -> None:

        for df_name in df_name_list:

            print(f"Checking if data {df_name} were already processed...", end=' ')
            if not df_name in self.loaded_dfs:
                print("No.")
                print("Getting data from remote database...", end=' ')
                df = self.dataset.get_dataframe(df_name)
                self.loaded_dfs[df_name] = df.copy()
                print("Done.")
            else:
                print("Yes.")
        
    
    def __export_to_csv(self, df, name) -> None:
    
        path = f'./data/{name}.csv'
        print(f"Saving data to {path} ...", end=' ')
        df.to_csv(path)
        print(f"Done.")


    def query_a1(self, name, export=False) -> pd.DataFrame:
        
        df_name_list = ['nakazeny_kraj']
        self.__load_dfs(df_name_list)
       
        df = self.loaded_dfs['nakazeny_kraj'].copy()
        df = df[['vek', 'kraj_nuts_kod']].rename({'vek': 'Vek', 'kraj_nuts_kod': 'Kraj'}, axis='columns')

        if export:
            self.__export_to_csv(df, name)

        return df


    def query_a2(self, name, export=False) -> pd.DataFrame:
        
        df_name_list = ['hospitalizovany', 'statistika_celkovo']
        self.__load_dfs(df_name_list)

        df1 = self.loaded_dfs['hospitalizovany'].copy()
        df1 = df1.groupby(pd.Grouper(key='datum', freq='M')).sum()[['pacient_prvni_zaznam']]

        df2 = self.loaded_dfs['statistika_celkovo'].copy()
        df2 = df2.groupby(pd.Grouper(key='datum', freq='M')).sum()[['prirustkovy_pocet_nakazenych',
                                                                    'prirustkovy_pocet_vylecenych',
                                                                    'prirustkovy_pocet_provedenych_testu']]
        df = pd.concat([df1, df2], axis='columns').reset_index()
        df = df.melt('datum', var_name='cols', value_name='vals')
        
        if export:
            self.__export_to_csv(df, name)
        
        return df 


    def query_b(self, name, export=False) -> List: 
        
        df_name_list = ['obyvatelia', 'nakazeny_kraj']
        self.__load_dfs(df_name_list)

        
        df1 = self.loaded_dfs['obyvatelia'].copy()
        last_year_total = pd.to_datetime(df1['casref_do'].unique()).year[-1]
        df1 = df1[(df1['vuzemi_cis'] == '100') & \
                  (df1['vek_cis'] == '0.0') & \
                  (df1['pohlavi_cis'] == '0.0') & \
                  (df1['casref_do'].dt.year.eq(last_year_total))].set_index('vuzemi_txt')
        
        df2 = self.loaded_dfs['nakazeny_kraj'].copy()
        df2 = df2.groupby([pd.Grouper(key='datum', freq='3M'), 
                           'kraj_nuts_kod']).size().reset_index(name='infected_per_month')
        df2 = df2[df2['kraj_nuts_kod'] != '0'].set_index('kraj_nuts_kod')

        df_list = []

        for date in df2.datum.unique():
            df = df2[df2.datum == date]
            df['total_people'] = df1.hodnota
            df['metric'] = df.infected_per_month / df.total_people
            df = df.sort_values(['metric'], ascending=False)
            df_list.append(df)

        df_list = df_list[-4:]
        
        if export:
            for idx, df in enumerate(df_list): self.__export_to_csv(df, f"{name}_quarter_{idx}")

        return df_list


    def query_custom1(self, name, months=12, export=False) -> List:

        df_name_list = ['hospitalizovani_ockovanie', 'zemreli_ockovanie', 'jip_ockovanie',
                        'ockovanie_kraj', 'obyvatelia']
        self.__load_dfs(df_name_list)
        
        df1 = self.loaded_dfs['obyvatelia']
        last_year_total = pd.to_datetime(df1['casref_do'].unique()).year[-1]
        df1 = df1[(df1['vuzemi_cis'] == '100') & \
                  (df1['vek_cis'] == '0.0') & \
                  (df1['pohlavi_cis'] == '0.0') & \
                  (df1['casref_do'].dt.year.eq(last_year_total))]
        ppl = df1.sum()['hodnota']

        df2 = self.loaded_dfs['ockovanie_kraj']
        df2 = df2.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:]
        vaccines = df2.druhych_davek / ppl
        vaccines = vaccines.reset_index()
        for i in range(1, len(vaccines)): 
            vaccines.loc[i, 'druhych_davek'] += vaccines.loc[i-1, 'druhych_davek']


        name_list = ['jip', 'zemreli', 'hospitalizovani']
        df_vaxxed_list = []
        df_unvaxxed_list = []

        for column_name in name_list:
            df = self.loaded_dfs[f'{column_name}_ockovanie']
            c_name_vaxxed = f'{column_name}_dokoncene_ockovani'
            c_name_unvaxxed = f'{column_name}_bez_ockovani'
            c_name_total = f'{column_name}_celkem'

            df_vaxxed = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_vaxxed]]
            df_unvaxxed = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_unvaxxed]]
            df_total = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_total]]
            
            df_vaxxed[c_name_vaxxed] /= df_total[c_name_total]
            df_unvaxxed[c_name_unvaxxed] /= df_total[c_name_total]

            df_vaxxed_list.append(df_vaxxed)
            df_unvaxxed_list.append(df_unvaxxed)

        vaxxed = pd.concat(df_vaxxed_list, axis='columns').reset_index().melt('datum',
                                                                              var_name='Typ',
                                                                              value_name='Percent')
        unvaxxed = pd.concat(df_vaxxed_list,axis='columns').reset_index().melt('datum',
                                                                               var_name='Typ',
                                                                               value_name='Percent')


        df_list = [vaxxed, unvaxxed, df2]

        if export:
            for idx, df in enumerate(df_list): self.__export_to_csv(df, f"{name}_{idx}")

        return df_list


    def query_custom2(self, name, export=False) -> pd.DataFrame:
        
        df_name_list = ['hospitalizovany', 'statistika_celkovo']
        self.__load_dfs(df_name_list)
        
        df_list = []
        for df_name in df_name_list:
            df = self.loaded_dfs[df_name]
            df = df.groupby(pd.Grouper(key="datum", freq="M")).sum()
            df_list.append(df)
        
        df = pd.concat(df_list, axis='columns')[['jip', 'kyslik', 'upv', 
                                                 'ecmo', 'tezky_upv_ecmo',
                                                 'prirustkovy_pocet_nakazenych']].reset_index()
        df = df.melt('datum', var_name='Kategorie', value_name='Pocet')

        if export:
            self.__export_to_csv(df, f"{name}")
        
        return df


if __name__ == "__main__":
    

    dataset = Dataset(name='proj_db')
    queries = Query(dataset=dataset)

    args = parse_args()

    for q_name in args.query_list:
        func = getattr(queries, q_name)
        df = func(name=q_name, export=True)
        


