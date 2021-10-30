import json
from dataset import Dataset


with open('datasets.json') as file:
    datasets = json.load(file)


dataset = Dataset(name='proj_db')
dataset.clear()

for item in datasets['sources']:
    dataset.download_and_insert(**item)

print(dataset.get_dataframe('okresy'))
