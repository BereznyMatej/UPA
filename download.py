import json
import argparse
from dataset import Dataset

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', type=str, help="Updates the specified collection in db. Use 'all' for updating every collection")
parser.add_argument('-d', '--download', action="store_true", help="Clears the database and downloads datasets stored in datasets.json")
parser.add_argument('-c', '--clear', action="store_true", help="Clears the database")
parser.add_argument('-s', '--fetch', type=str, help="Fetches the specified collection from db")
args = parser.parse_args()


with open('datasets.json') as file:
    metadata = json.load(file)

dataset = Dataset(name='proj_db')

if args.clear or args.download:
    dataset.clear()

if args.download or args.update == 'all':
    for item in metadata['sources']:
        dataset.clear(collection_name=item['name'])
        dataset.download_and_insert(**item)
elif args.update:
    for item in metadata['sources']:
         if item == args.update:
            dataset.clear(collection_name=item['name'])
            dataset.download_and_insert(**item)


if args.fetch:
    print(dataset.get_dataframe(args.fetch))
