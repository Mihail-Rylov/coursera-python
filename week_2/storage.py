import os
import tempfile
from json import loads, dumps
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        result = f.read()
        if result:
            return loads(result)

        return {}


def put(key, value):
    data = get_data()
    data[key] = data.get(key, list())
    data[key].append(value)

    with open(storage_path, 'w') as f:
        f.write(dumps(data))

def get(key):
    data = get_data()
    if key in data:
        return data[key]
    else:
        return None

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

if args.key and args.val:
    put(args.key, args.val)
elif args.key:
    print(get(args.key))
