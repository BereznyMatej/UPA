import pandas as pd
import numpy as np
import json
import requests
import os

from ssh_pymongo import MongoSession

class Dataset:

    def __init__(self, name):
        """Sets up the connection between remote db and local client.

        Args:
            name (str): mongo database name
        """
        self.types = {'date': np.datetime64,
                      'integer': np.uint32,
                      'string': str,
                      'boolean': bool}
        self.session = MongoSession(host='ec2-13-40-24-161.eu-west-2.compute.amazonaws.com',
                                    user='ubuntu',
                                    key='UPA-projekt.pem')
        self.client = self.session.connection
        self.name = name
        self.db = self.client[self.name]
        self.region_mapper = {'CZ010': 'Praha',
                              'CZ020': 'Stredocesky kraj',
                              'CZ031': 'Jihocesky kraj',
                              'CZ032': 'Plzensky kraj',
                              'CZ041': 'Karlovarsky kraj',
                              'CZ042': 'Ustecky kraj',
                              'CZ051': 'Liberecky kraj',
                              'CZ052': 'Kralovohradecky kraj',
                              'CZ053': 'Pardubicky kraj',
                              'CZ063': 'Kraj Vysocina',
                              'CZ064': 'Jihomoravsky kraj',
                              'CZ071': 'Olomoucky kraj',
                              'CZ072': 'Zlinsky kraj',
                              'CZ080': 'Moravskoslezsky kraj'}

    def clear(self, collection_name=None):
        """Clears one collection from remote db if collection_name is specified, otherwise wipes the entire database. 

        Args:
            collection_name (str, optional): name of the collection to be cleared. Defaults to None.
        """
        if collection_name is not None:
            self.db[collection_name].drop()
        else:
            self.client.drop_database(self.name)
            self.db = self.client[self.name]


    def download_and_insert(self, name, url, schema_url):
        """Downloads the data (& schema if its not already present in db) from urls specified in params
        and inserts them into the db.

        Args:
            name (str): name under which collection will be stored in db
            url (str): link for downloading data
            schema_url (str): link for downloading schema for aforementioned data
        """
        print(f"Processing {name}... ", end=' ')
        schema_name = f"{name}_schema"

        schema = self.get(schema_name)
        
        if not schema:
            schema = requests.get(schema_url, headers={'user-agent' : ""}).json()
            self.__save_schema(schema, schema_name)
        else:
            schema = schema['data']

        data = self.parse(pd.read_csv(url), schema)

        self.insert(data, name)
        print("Done.")


    def parse(self, data, schema):
        """Transforms datatypes loaded from db/.csv files to more fitting ones according to the 
        informations stored in schema collections.

        Args:
            data (pd.DataFrame): dataframe containing data
            schema (dict): schema dictionary containing column:datatype pairs

        Returns:
            pd.DataFrame: processed dataframe with correct datatypes
        """
        data = data.fillna(0)
        data = data.astype({item['name']: self.types[item['datatype']] for item in schema['tableSchema']['columns']})
        
        if 'kraj_nuts_kod' in data:
            data = data.replace({'kraj_nuts_kod': self.region_mapper}).rename({'kraj_nuts_kod': 'Kraj'}, axis='columns')

        return data
    

    def __save_schema(self, schema, name):
        """Stores schema as a whole into the remote db.

        Args:
            schema (dict): schema dictionary containing column:datatype pairs
            name (str): name under which schema will be stored in db
        """
        table = self.db[name]
        table.insert_one(schema)


    def get_dataframe(self, name):
        """Loads both dataframe & schema from database and 

        Args:
            name (str): collection name

        Returns:
            pd.DataFrame: processed dataframe with correct datatypes
        """
        schema = self.get(f"{name}_schema")['data']
        data = pd.DataFrame(iter(self.get(name)))
        return self.parse(data, schema)


    def get(self, name):
        """Retrieves specified collection from database.

        Args:
            name (str): collection name

        Returns:
            pymongo.cursor.Cursor/dict: retrieved collection
        """
        table = self.db[name]
        data = table.find_one() if 'schema' in name else table.find()
        return data


    def insert(self, data, name):
        """Inserts dataframe into the remote db.

        Args:
            data (pd.DataFrame): dataframe containing data
            name (str): name under which collection will be stored in db
        """
        table = self.db[name]
        data.index = data.index.map(str)
        table.insert_many(data.to_dict('records'))
