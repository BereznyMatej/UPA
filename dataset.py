import pandas as pd
import numpy as np
import json
import requests
import pymongo
import os


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
        self.client = pymongo.MongoClient('mongodb+srv://Admin:klat8klat@upa.85xuv.mongodb.net/UPA?retryWrites=true&w=majority', 27017, maxPoolSize=50)
        self.name = name
        self.db = self.client[self.name]
        

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
