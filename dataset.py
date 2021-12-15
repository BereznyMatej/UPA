import threading
import pandas as pd
import numpy as np
import json
import requests

from pymongo import MongoClient

class Dataset:

    types = {'date': np.datetime64,
             'integer': np.uint32,
             'number': np.uint32,
             'string': str,
             'boolean': bool}
    region_mapper = {'CZ010': 'Hlavní město Praha',
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


    def __init__(self, name, workers):
        """Sets up the connection between remote db and local client.

        Args:
            name (str): mongo database name
        """
        self.name = name
        self.connection_string = "mongodb://ubuntu:klat8klat@ec2-13-40-24-161.eu-west-2.compute.amazonaws.com:27017/{}?authSource=admin".format(self.name)
        self.workers = workers
        self.client = MongoClient(self.connection_string)
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


    def download_and_insert(self, name, url, schema_url, update=False):
        """Downloads the data (& schema if its not already present in db) from urls specified in params
        and inserts them into the db.

        Args:
            name (str): name under which collection will be stored in db
            url (str): link for downloading data
            schema_url (str): link for downloading schema for aforementioned data
            update (bool): if True, updates the existing table instead of only downloading new one
        """
        print(f"Processing {name}... ")
        schema_name = f"{name}_schema"

        schema = self.get(schema_name)
        old_data = None

        if not schema:
            schema = requests.get(schema_url, headers={'user-agent' : ""}).content.decode('utf-8-sig')
            schema = json.loads(schema)['tableSchema']
            schema['columns'].pop(0)
            self.__save_schema(schema, schema_name)
        else:
            schema = schema

        data = pd.read_csv(url, index_col=0)
        data.index.names = ['_id']

        if update:
            old_data = self.get_dataframe(name)

        data = np.array_split(data, self.workers)

        threads = []

        for idx, item in enumerate(data):
            threads.append(ProcessingThread(conn_string=self.connection_string,
                                            db_name=self.name, 
                                            name=name,
                                            idx=idx,
                                            data=item,
                                            schema = schema,
                                            update=update,
                                            old_data=old_data))
            threads[idx].start()

        for t in threads:
            t.join()

        print("Done.")



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


    @classmethod
    def parse(cls, data, schema):
        """Transforms datatypes loaded from db/.csv files to more fitting ones according to the 
        informations stored in schema collections.

        Args:
            data (pd.DataFrame): dataframe containing data
            schema (dict): schema dictionary containing column:datatype pairs

        Returns:
            pd.DataFrame: processed dataframe with correct datatypes
        """
        data = data.fillna(0)
        data = data.astype({item['name']: cls.types[item['datatype']] for item in schema['columns']})
        
        if 'kraj_nuts_kod' in data:
            data = data.replace({'kraj_nuts_kod': cls.region_mapper})

        if 'datum' in data:
            data['datum'] = pd.to_datetime(data['datum'])
        elif 'casref_do' in data:
            data['casref_do'] = pd.to_datetime(data['casref_do'])

        return data

    @classmethod
    def insert(cls, data, table):
        """Inserts dataframe into the remote db.

        Args:
            data (pd.DataFrame): dataframe containing data
            name (str): name under which collection will be stored in db
        """
        
        if not data.empty:
            table.insert_many(data.reset_index().to_dict('records'))
        

class ProcessingThread(threading.Thread):


    def __init__(self, conn_string, db_name, name, idx, data, schema, 
                 update=False, old_data=None):
        threading.Thread.__init__(self)
        self.client = MongoClient(conn_string)
        self.db = self.client[db_name]
        self.name = name
        self.idx = idx
        self.schema = schema
        self.data = data
        self.update = update
        self.old_data = old_data


    def run(self):

        data = Dataset.parse(self.data, self.schema)

        if self.update:
            data = data[~data.isin(self.old_data)].dropna()

        table = self.db[self.name]
        Dataset.insert(data, table)

        print(f"Worker {self.idx} has finished uploading {self.name}")

