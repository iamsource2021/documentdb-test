import json
from math import dist
import os
import pymongo
import clientmongodb

from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()


def insert_one(doc):
    try:
        client = clientmongodb.client_mongo(
            os.environ['MONGODB_CLOUD_DEFAULT'])
        db = client['test']
        profiles = db['profiles']
        return profiles.insert_one(doc)

    except Exception as e:
        raise Exception(str(e))


def handler(event, context):
    input =event['arguments']['input']
    insert_one(input)    
    del input['_id']
    return input
