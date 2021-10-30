import pandas as pd
import numpy as np
import json
import requests
import pymongo
import os


class Dataset:

    def __init__(self, name):
        self.types = {'date': np.datetime64,
                      'integer': np.uint32,
                      'string': str,
                      'boolean': bool}
        self.client = pymongo.MongoClient('mongodb+srv://Admin:klat8klat@upa.85xuv.mongodb.net/UPA?retryWrites=true&w=majority', 27017, maxPoolSize=50)
        self.name = name
        self.db = self.client[self.name]
        

    def clear(self):
        self.client.drop_database(self.name)
        self.db = self.client[self.name]


    def download_and_insert(self, name, url, schema_url):

        print(f"Processing {name}... ", end='')
        schema_name = f"{name}_schema"

        schema = self.get(schema_name)
        
        if not schema:
            schema = requests.get(schema_url, headers={'user-agent' : ""}).json()
            self.__save_schema(schema, schema_name)
        
        data = self.parse(pd.read_csv(url), schema)
        self.insert(data, name)
        print("Done.")


    def parse(self, data, schema):
        data = data.fillna(0)
        data = data.astype({item['name']: self.types[item['datatype']] for item in schema['tableSchema']['columns']})
        return data
    

    def __save_schema(self, schema, name):
        table = self.db[name]
        table.insert_one(schema)


    def get_dataframe(self, name):
        
        schema = self.get(f"{name}_json")
        data = pd.DataFrame(self.get(name))
        return self.parse(data, schema)


    def get(self, name):
        table = self.db[name]
        data = list(table.find())

        return data[0] if data else []


    def insert(self, data, name):
        
        table = self.db[name]
        data.index = data.index.map(str)
        table.insert_many(data.to_dict('records'))
