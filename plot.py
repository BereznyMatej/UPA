import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick
import pandas as pd
import argparse
import os

from prepare_data import QueryParser
from dataset import Dataset


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query_list', nargs='+', required=True, type=str)
    return parser.parse_args()


class QueryPlotter:

    def __init__(self, dataset) -> None:
        """Plots the preprocessed data accordingly to information provided in assignment.

        Args:
            dataset (Dataset): 
        """
        self.parser = QueryParser(dataset)
        sns.set(style="whitegrid")
    

    def __export_to_png(self, fig, name):
        """Exports plot to .png file.

        Args:
            fig (matplotlib.Figure):
            name (str): query name
        """
        fig.tight_layout()
        plt_name = f"plts/{name}.png"
        fig.savefig(plt_name)
        print(f"Saving plot to '{plt_name}'")


    def __load_csv(self, name):
        """Loads the .csv file into dataframe. If there is no .csv file present, 
           attempts to create it via QueryParser

        Args:
            name (str): query_name

        Returns:
            list: list of the loaded dataframes
        """
        csv_list = [item for item in os.listdir('data') if name in item]
        df_list = []

        if not csv_list:
            func = getattr(self.parser, name)
            func(name=name, export=True)
            return self.__load_csv(name)

        for item in csv_list:
            df_list.append(pd.read_csv(f"data/{item}"))
        return df_list


    def query_a2(self, name):
        """Plots the graph from data prepared by QueryParser. For detailed description of the graph itself
        please refer to documentation.

        Args:
            name (str): query name
        """
        fig, ax = plt.subplots(figsize=(20, 10))

        df = self.__load_csv(name)[0]
        df = df.loc[df.index.repeat(df.Count)]
        sns.boxplot(data=df, x='Region', y='Age', ax=ax)
        
        ax.tick_params(axis='x', rotation=45)  
        fig.suptitle('Age distribution of covid-19 positive patients by region', fontsize=18)

        self.__export_to_png(fig, name)


    def query_a1(self, name):
        """Plots the graph from data prepared by QueryParser. For detailed description of the graph itself
        please refer to documentation.

        Args:
            name (str): query name
        """        
        fig, ax = plt.subplots(figsize=(20, 10))

        df = self.__load_csv(name)[0]
        sns.lineplot(data=df, x='Date', y='Count', hue='Category', ax=ax)

        ax.set(yscale='log')
        ax.set(xlim=(df.Date.unique()[0], df.Date.unique()[-2]))
        ax.tick_params(axis='x', rotation=45)  
        fig.suptitle('Covid-19 development throughout the time', fontsize=18)

        self.__export_to_png(fig, name)


    def query_b(self, name, quarter=1):
        """Plots the graph from data prepared by QueryParser. For detailed description of the graph itself
        please refer to documentation.

        Args:
            name (str): query name
            quarter (int, optional): determines which quarter of the 4 processed will be plotted
        """
        fig, ax = plt.subplots(figsize=(20, 10))

        df = self.__load_csv(name)[quarter]
        df = df.melt('Region', var_name='Category', value_name='Count')        
        sns.barplot(data=df[df.Category == 'total_people'].reset_index(), 
                    x='Region', y='Count', color='lightblue',
                    ax=ax)
        sns.barplot(data=df[df.Category == 'infected_per_month'].reset_index(),
                    x='Region', y='Count', color='darkblue', ax=ax)
        
        ax.tick_params(axis='x', rotation=45)  
        ax.set(yscale='log')
        ax1 = ax.twinx()
        fig.suptitle('Covid-19 positive cases per total population in regions.', fontsize=18)

        sns.lineplot(data=df[df.Category == 'metric'].reset_index(), y='Count',
                     x='Region', ax=ax1, color='red', marker="o")

        bottom_bar = mpatches.Patch(color='darkblue', label='Covid-19 positive')
        top_bar = mpatches.Patch(color='lightblue', label='Total people')
        line = mpatches.Patch(color='red', label='Covid-19 positive / Total people')
        plt.legend(handles=[top_bar, bottom_bar, line])

        self.__export_to_png(fig, name)


    def query_custom1(self, name):
        """Plots the graph from data prepared by QueryParser. For detailed description of the graph itself
        please refer to documentation.

        Args:
            name (str): query name
        """
        fig, ax = plt.subplots(figsize=(20, 10))

        dfs = self.__load_csv(name)
        sns.barplot(data=dfs[1], x='Date', y='Percent', hue='Category',
                    palette=sns.color_palette("Blues"), ax=ax)
        sns.barplot(data=dfs[0], x='Date', y='Percent', hue='Category',
                    palette=sns.color_palette("Blues_r"), ax=ax)
        
        ax.set_yticklabels(['{:,.2%}'.format(x) for x in ax.get_yticks()])
        ax.tick_params(axis='x', rotation=45) 
        ax1 = ax.twiny()
        ax1.set_xticks([])
        fig.suptitle('Death/ICU/Hospitalized Ratio between vaccinated & unvaccinated people', fontsize=18)

        sns.lineplot(data=dfs[2], x='Date', y='Vaccinated %', color='red',
                     ax=ax1, marker="o")

        self.__export_to_png(fig, name)


    def query_custom2(self, name):
        """Plots the graph from data prepared by QueryParser. For detailed description of the graph itself
        please refer to documentation.

        Args:
            name (str): query name
        """
        fig, ax = plt.subplots(figsize=(20, 10))

        df = self.__load_csv(name)[0]
        sns.lineplot(data=df, x='Date', y='Count', hue='Category')

        fig.suptitle('Comparison between new critical cases and overall new covid-19 cases.', fontsize=18)
        ax.tick_params(axis='x', rotation=45)  
        ax.set(xlim=(df.Date.unique()[0], df.Date.unique()[-2]))

        self.__export_to_png(fig, name)


if __name__ == "__main__":

    dataset = Dataset(name='proj_db')
    queries = QueryPlotter(dataset=dataset)

    args = parse_args()

    for q_name in args.query_list:
        func = getattr(queries, q_name)
        func(name=q_name)
        
