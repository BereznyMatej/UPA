import json
from dataset import Dataset


with open('datasets.json') as file:
    datasets = json.load(file)


dataset = Dataset(name='proj_db')


for item in datasets['sources']:
    dataset.download_and_insert(**item)


