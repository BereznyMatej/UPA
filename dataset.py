import pandas as pd
import numpy as np
import json
import requests

from ssh_pymongo import MongoSession

class Dataset:

    def __init__(self, name):
        """Sets up the connection between remote db and local client.

        Args:
            name (str): mongo database name
        """
        self.types = {'date': np.datetime64,
                      'integer': np.uint32,
                      'number': np.uint32,
                      'string': str,
                      'boolean': bool}
        self.session = MongoSession(host='ec2-13-40-24-161.eu-west-2.compute.amazonaws.com',
                                    user='ubuntu',
                                    key='UPA-projekt.pem')
        self.client = self.session.connection
        self.name = name
        self.db = self.client[self.name]
        self.region_mapper = {'CZ010': 'Hlavní město Praha',
                              'CZ020': 'Středočeský kraj',
                              'CZ031': 'Jihočeský kraj',
                              'CZ032': 'Plzeňský kraj',
                              'CZ041': 'Karlovarský kraj',
                              'CZ042': 'Ústecký kraj',
                              'CZ051': 'Liberecký kraj',
                              'CZ052': 'Královéhradecký kraj',
                              'CZ053': 'Pardubický kraj',
                              'CZ063': 'Kraj Vysočina',
                              'CZ064': 'Jihomoravský kraj',
                              'CZ071': 'Olomoucký kraj',
                              'CZ072': 'Zlínský kraj',
                              'CZ080': 'Moravskoslezský kraj'}

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


    def download_and_insert(self, name, url, schema_url, update=False):
        """Downloads the data (& schema if its not already present in db) from urls specified in params
        and inserts them into the db.

        Args:
            name (str): name under which collection will be stored in db
            url (str): link for downloading data
            schema_url (str): link for downloading schema for aforementioned data
            update (bool): if True, updates the existing table instead of only downloading new one
        """
        print(f"Processing {name}... ", end=' ')
        schema_name = f"{name}_schema"

        schema = self.get(schema_name)
        
        if not schema:
            schema = requests.get(schema_url, headers={'user-agent' : ""}).content.decode('utf-8-sig')
            schema = json.loads(schema)['tableSchema']
            schema['columns'].pop(0)
            self.__save_schema(schema, schema_name)
        else:
            schema = schema

        data = pd.read_csv(url, index_col=0)
        data.index.names = ['_id']
        data = self.parse(data, schema)

        if update:
            old_data = self.get_dataframe(name)
            data = data[~data.isin(old_data)].dropna()

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
        data = data.astype({item['name']: self.types[item['datatype']] for item in schema['columns']})
        
        if 'kraj_nuts_kod' in data:
            data = data.replace({'kraj_nuts_kod': self.region_mapper})

        if 'datum' in data:
            data['datum'] = pd.to_datetime(data['datum'])
        elif 'casref_do' in data:
            data['casref_do'] = pd.to_datetime(data['casref_do'])

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
        schema = self.get(f"{name}_schema")
        data = pd.DataFrame(iter(self.get(name)))
        data = data.set_index(data.columns[0])
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
        if not data.empty:
            table = self.db[name]
            table.insert_many(data.reset_index().to_dict('records'))
    

    def __delete__(self):
        self.session.close()