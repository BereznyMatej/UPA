from typing import List
from matplotlib.pyplot import axes
import pandas as pd
import numpy as np
import argparse

from dataset import Dataset

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query_list', nargs='+', required=True, type=str)
    return parser.parse_args()
    

class QueryParser:

    def __init__(self, dataset) -> None:
        """Gets the required data from db, processes them and saves into dedicated .csv files.

        Args:
            dataset (Dataset):
        """
        self.dataset = dataset
        self.loaded_dfs = {}


    def __load_dfs(self, df_name_list) -> None:
        """Loads the collections and saves them into self.loaded_dfs dictionary.

        Args:
            df_name_list (list): list containing collection names
        """
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
        """Exports dataframe to .csv file

        Args:
            df (pd.Dataframe): dataframe containing data to be exported
            name (str): name of the .csv file
        """
        path = f'./data/{name}.csv'
        print(f"Saving data to {path} ...", end=' ')
        df.to_csv(path)
        print(f"Done.")


    def query_a2(self, name, export=False) -> pd.DataFrame:
        """Prepares data for query A-2. For futher describtion, refer to documentation.

        Args:
            name (str): query name
            export (bool, optional): If True, dataframe will be exported to .csv file. Defaults to False.

        Returns:
            pd.DataFrame: processed dataframe
        """
        df_name_list = ['nakazeny_kraj']
        self.__load_dfs(df_name_list)
       
        df = self.loaded_dfs['nakazeny_kraj'].copy()
        df = df.groupby(['kraj_nuts_kod', 'vek']).size().reset_index(name='Count')
        df = df[['vek', 'kraj_nuts_kod', 'Count']].rename({'vek': 'Age', 'kraj_nuts_kod': 'Region'}, axis='columns')
        df = df[df['Region'] != '0']

        if export:
            self.__export_to_csv(df, name)

        return df


    def query_a1(self, name, export=False) -> pd.DataFrame:
        """Prepares data for query A-1. For futher description, refer to documentation.

        Args:
            name (str): query name
            export (bool, optional): If True, dataframe will be exported to .csv file. Defaults to False.

        Returns:
            pd.DataFrame: processed dataframe
        """
        df_name_list = ['hospitalizovany', 'statistika_celkovo']
        self.__load_dfs(df_name_list)

        df1 = self.loaded_dfs['hospitalizovany'].copy()
        df1 = df1.groupby(pd.Grouper(key='datum', freq='M')).sum()[['pacient_prvni_zaznam']]

        df2 = self.loaded_dfs['statistika_celkovo'].copy().reset_index().rename({'_id': 'datum'},
                                                                                axis='columns')
        df2['datum'] = pd.to_datetime(df2['datum'])
        df2 = df2.groupby(pd.Grouper(key='datum', freq='M')).sum()[['prirustkovy_pocet_nakazenych',
                                                                    'prirustkovy_pocet_vylecenych',
                                                                    'prirustkovy_pocet_provedenych_testu']]
        df = pd.concat([df1, df2], axis='columns').reset_index()
        df = df.rename({'datum': 'Date', 
                        'prirustkovy_pocet_nakazenych': 'Positive',
                        'prirustkovy_pocet_vylecenych': 'Recovered',
                        'prirustkovy_pocet_provedenych_testu': 'Tests',
                        'pacient_prvni_zaznam': 'Hospitalized'},
                       axis='columns')
        df = df.melt('Date', var_name='Category', value_name='Count')
        
        if export:
            self.__export_to_csv(df, name)
        
        return df 


    def query_b(self, name, export=False) -> List: 
        """Prepares data for query B. For futher description, refer to documentation.

        Args:
            name (str): query name
            export (bool, optional): If True, dataframe will be exported to .csv file. Defaults to False.

        Returns:
            List: list of processed dataframe
        """
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
                           'kraj_nuts_kod']).size().reset_index(name='infected_per_month').reset_index()
        df2 = df2.rename({'kraj_nuts_kod': 'Region', 'datum': 'Date'}, axis='columns')
        df2 = df2[df2['Region'] != '0'].set_index('Region')
        df_list = []

        for date in df2.Date.unique():
            df = df2[df2.Date == date]
            df['total_people'] = df1.hodnota
            df['metric'] = df.infected_per_month / df.total_people
            df = df.sort_values(['metric'], ascending=False)
            df_list.append(df)

        df_list = df_list[-4:]
        
        if export:
            for idx, df in enumerate(df_list): self.__export_to_csv(df, f"{name}_quarter_{idx}")

        return df_list


    def query_custom1(self, name, months=12, export=False) -> List:
        """Prepares data for custom query. For futher description, refer to documentation.

        Args:
            name (str): query name
            months (int, optional): For how many months data should be processed. Defaults to 12.
            export (bool, optional): [description]. Defaults to False.

        Returns:
            List: list of processed dataframe
        """
        df_name_list = ['hospitalizovani_ockovanie', 'zemreli_ockovanie', 'jip_ockovanie',
                        'ockovanie_kraj', 'obyvatelia']
        self.__load_dfs(df_name_list)
        
        df1 = self.loaded_dfs['obyvatelia'].copy()
        last_year_total = pd.to_datetime(df1['casref_do'].unique()).year[-1]
        df1 = df1[(df1['vuzemi_cis'] == '100') & \
                  (df1['vek_cis'] == '0.0') & \
                  (df1['pohlavi_cis'] == '0.0') & \
                  (df1['casref_do'].dt.year.eq(last_year_total))]
        ppl = df1.sum()['hodnota']

        df2 = self.loaded_dfs['ockovanie_kraj'].copy()
        df2['datum'] = pd.to_datetime(df2['datum'])
        df2 = df2.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:]
        vaccines = df2.druhych_davek / ppl
        vaccines = vaccines.reset_index().rename({'datum': 'Date', 'druhych_davek': 'Vaccinated %'},
                                                  axis='columns')
        for i in range(1, len(vaccines)): 
            vaccines.loc[i, 'Vaccinated %'] += vaccines.loc[i-1, 'Vaccinated %']


        name_list = ['jip', 'zemreli', 'hospitalizovani']
        eng_name_lsit = ['ICU', 'Deaths', 'Hospitalized']
        df_vaxxed_list = []
        df_unvaxxed_list = []

        for idx, column_name in enumerate(name_list):
            df = self.loaded_dfs[f'{column_name}_ockovanie'].copy()
            c_name_vaxxed = f'{column_name}_dokoncene_ockovani'
            c_name_unvaxxed = f'{column_name}_bez_ockovani'
            c_name_total = f'{column_name}_celkem'

            df_vaxxed = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_vaxxed]]
            df_unvaxxed = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_unvaxxed]]
            df_total = df.groupby(pd.Grouper(key='datum', freq='M')).sum()[-months:][[c_name_total]]
            
            df_vaxxed[c_name_vaxxed] /= df_total[c_name_total]
            df_unvaxxed[c_name_unvaxxed] /= df_total[c_name_total]

            df_vaxxed = df_vaxxed.rename({c_name_vaxxed: f'{eng_name_lsit[idx]} - Vaccinated'}, axis='columns')
            df_unvaxxed = df_unvaxxed.rename({c_name_unvaxxed: f'{eng_name_lsit[idx]} - Unvaccinated'}, axis='columns')

            df_vaxxed_list.append(df_vaxxed)
            df_unvaxxed_list.append(df_unvaxxed)

        vaxxed = pd.concat(df_vaxxed_list,
                           axis='columns').reset_index().rename({'datum': 'Date'},
                                                                axis='columns').melt('Date',
                                                                                     var_name='Category',
                                                                                     value_name='Percent')
        unvaxxed = pd.concat(df_unvaxxed_list,
                             axis='columns').reset_index().rename({'datum': 'Date'},
                                                                  axis='columns').melt('Date',
                                                                                       var_name='Category',
                                                                                       value_name='Percent')
        df_list = [vaxxed, unvaxxed, vaccines]

        if export:
            for idx, df in enumerate(df_list): self.__export_to_csv(df, f"{name}_{idx}")

        return df_list


    def query_custom2(self, name, export=False) -> pd.DataFrame:
        """Prepares data for custom query 2. For futher description, refer to documentation.

        Args:
            name (str): query name
            export (bool, optional): If True, dataframe will be exported to .csv file. Defaults to False.

        Returns:
            pd.DataFrame: processed dataframe
        """
        df_name_list = ['hospitalizovany', 'statistika_celkovo']
        self.__load_dfs(df_name_list)
        
   
        df1 = self.loaded_dfs['hospitalizovany'].copy()
        df1 = df1.groupby(pd.Grouper(key="datum", freq="M")).sum()

        df2 = self.loaded_dfs['statistika_celkovo'].copy().reset_index().rename({'_id': 'datum'},
                                                                                axis='columns')
        df2['datum'] = pd.to_datetime(df2['datum'])
        df2 = df2.groupby(pd.Grouper(key="datum", freq="M")).sum()
        
        df = pd.concat([df1, df2], axis='columns')[['jip', 'kyslik', 'upv', 
                                                    'ecmo', 'tezky_upv_ecmo',
                                                    'prirustkovy_pocet_nakazenych']].reset_index()
        df = df.rename({'datum': 'Date',
                        'prirustkovy_pocet_nakazenych': 'New cases',
                        'jip': 'Intensive care unit',
                        'kyslik':'Oxygen',
                        'upv': 'Artificial lung ventilation',
                        'ecmo': 'ECMO',
                        'tezky_upv_ecmo': 'ALV + ECMO'},
                        axis='columns')
        df = df.melt('Date', var_name='Category', value_name='Count')

        if export:
            self.__export_to_csv(df, f"{name}")
        
        return df
    
    def query_c(self, name, export=False) -> pd.DataFrame:
        """Prepares data for query c. For futher description, refer to documentation.

        Args:
            name (str): query name
            export (bool, optional): If True, dataframe will be exported to .csv file. Defaults to False.

        Returns:
            pd.DataFrame: processed .csv file
        """
        df_name_list = ['obyvatelia', 'obce', 'ockovanie_zariadenia']

        self.__load_dfs(df_name_list)
        
        df = self.loaded_dfs['obyvatelia'].copy()
        df2 = self.loaded_dfs['obce'].copy()
        
        df3 = pd.read_csv('ockovaci-mista.csv', index_col=0)
        df3['zarizeni_kod'] = df3['zarizeni_kod'].astype(np.uint64)
        df4 = self.loaded_dfs['ockovanie_zariadenia'].copy()
        df4['zarizeni_kod'] = df4['zarizeni_kod'].astype(np.uint64)

        age_groups = [['0 až 5 (více nebo rovno 0 a méně než 5)',
                       '5 až 10 (více nebo rovno 5 a méně než 10)',
                       '10 až 15 (více nebo rovno 10 a méně než 15)'],
                       ['15 až 20 (více nebo rovno 15 a méně než 20)',
                       '20 až 25 (více nebo rovno 20 a méně než 25)',
                       '25 až 30 (více nebo rovno 25 a méně než 30)',
                       '30 až 35 (více nebo rovno 30 a méně než 35)',
                       '35 až 40 (více nebo rovno 35 a méně než 40)',
                       '40 až 45 (více nebo rovno 40 a méně než 45)',
                       '45 až 50 (více nebo rovno 45 a méně než 50)',
                       '50 až 55 (více nebo rovno 50 a méně než 55)',],
                       ['55 až 60 (více nebo rovno 55 a méně než 60)',
                       '60 až 65 (více nebo rovno 60 a méně než 65)',
                       '65 až 70 (více nebo rovno 65 a méně než 70)',
                       '70 až 75 (více nebo rovno 70 a méně než 75)',
                       '75 až 80 (více nebo rovno 75 a méně než 80)',
                       '80 až 85 (více nebo rovno 80 a méně než 85)',
                       '85 až 90 (více nebo rovno 85 a méně než 90)',
                       '90 až 95 (více nebo rovno 90 a méně než 95)',
                       'Od 95 (více nebo rovno 95)']]

        age_categories = ['Age [0-15]', 'Age [15-55]', 'Age [55+]']

        latest_date = pd.to_datetime(df['casref_do']).max()

        df = df.drop(df[df.casref_do != latest_date].index)

        df = df.drop(df[df.vek_txt == '0'].index)
        df = df.drop(df[df.pohlavi_txt != '0'].index)
        df = df.drop(df[df.vuzemi_cis == '97'].index)
        df = df.drop(df[df.vuzemi_cis == '100'].index)

        age_mapped = (pd.DataFrame({'vek_skupina': age_categories, 'vek_txt': age_groups})
                                                                    .explode('vek_txt')
                                                                    .reset_index(drop=True))

        df = df.merge(age_mapped, on='vek_txt', how='left').fillna("Other")

        df = df.drop(columns=['pohlavi_kod',
                              'pohlavi_cis',
                              'pohlavi_txt',
                              'vek_cis',
                              'vek_kod',
                              'casref_do',
                              'stapro_kod',
                              'vuzemi_cis',
                              'vuzemi_kod'])

        df = df.groupby(['vuzemi_txt', 'vek_skupina']).sum().reset_index()
        df = df.pivot_table(index='vuzemi_txt', columns='vek_skupina', values='hodnota')

        df2 = df2[['datum','okres_nazev']]

        df2['datum'] = pd.to_datetime(df2['datum'])

        df2 = df2[(df2['datum'] >= pd.Timestamp(year=2020, month=12, day=16, hour=12))]

        df2 = df2.groupby(['okres_nazev']).count()

        df2 = df2.iloc[1:]

        df['Infected'] = df2['datum']

        df3 = df3.merge(df4, on='zarizeni_kod', how='left')
        df3['datum'] = pd.to_datetime(df3.datum)
        df3 = df3.groupby([pd.Grouper(key='datum',
                                      freq='3M'),
                          'okres_nazev']).size().reset_index(name='Vaccinated')
        df3 = df3[(df3['datum'] >= df3.datum.unique()[-4])]
        df3 = df3.groupby('okres_nazev').sum()

        df = pd.concat([df, df3], axis='columns')

        df_unnormalized = df
        df_unnormalized = df_unnormalized.iloc[:50]

        df['Vaccination_percentage'] = (df['Vaccinated']/((df['Age [0-15]'] + df['Age [15-55]'] + df['Age [55+]']) / 100))

        discretization = [
            (df['Vaccination_percentage'] <= 10),
            (df['Vaccination_percentage'] > 10) & (df['Vaccination_percentage'] <= 25),
            (df['Vaccination_percentage'] > 25) & (df['Vaccination_percentage'] <= 50),
            (df['Vaccination_percentage'] > 50)]
        
        discretization_values = ['low', 'partial', 'about_a_quarter', 'above_a_half']

        df['Vaccination'] = np.select(discretization, discretization_values)

        df = df.iloc[:50]

        if export:
            self.__export_to_csv(df, f"{name}")
            self.__export_to_csv(df_unnormalized, f"{name}_unnormalized")
        
        return df


if __name__ == "__main__":
    

    dataset = Dataset(name='proj_db')
    queries = QueryParser(dataset=dataset)

    args = parse_args()

    for q_name in args.query_list:
        func = getattr(queries, q_name)
        df = func(name=q_name, export=True)
        


