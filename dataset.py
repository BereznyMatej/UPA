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
        self.client = pymongo.MongoClient("localhost", 27017, maxPoolSize=50)
        self.name = name
        self.db = self.client[self.name]
        
    
    def download_and_insert(self, name, url, schema_url):

        schema_name = f"schemas/{name}.json"
        
        if not os.path.isfile(schema_name):
            schema = requests.get(schema_url, headers={'user-agent' : ""}).json()
            self.__save_schema(schema, name)
        else:
            with open(f"schemas/{name}.json") as file:
                schema = json.load(file) 

        data = self.parse(pd.read_csv(url), schema)
        self.insert(data, name)


    def parse(self, data, schema):
        data = data.fillna(0)
        data = data.astype({item['name']: self.types[item['datatype']] for item in schema['tableSchema']['columns']})
        return data
    

    def __save_schema(self, schema, name):
        with open(f"schemas/{name}.json", 'w', encoding='utf8') as file:
            json.dump(schema, file, ensure_ascii=False)
            file.close()


    def get(self, name):

        with open(f"schemas/{name}.json") as file:
            schema = json.load(file) 

        table = self.db['Covid']
        data = pd.DataFrame(table.find_one({"index": name})['data'])
        return self.parse(data, schema)


    def insert(self, data, name):
        
        table = self.db['Covid']
        data = data.astype(str)
        data.index = data.index.map(str)
        data_dict = data.to_dict()
        table.insert_one({"index": name, "data": data.to_dict()})

        