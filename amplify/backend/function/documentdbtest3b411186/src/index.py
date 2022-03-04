import json
import os
import pymongo
import clientmongodb

from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()


def find():
    try:
        client = clientmongodb.client_mongo(
            os.environ['MONGODB_CLOUD_DEFAULT'])
        db = client['test']
        profiles = db['profiles']
        return profiles.find(
            {},
            {
                "nombre": 1,
                "razonsocial": 1,
                "rfc": 1,
                "direccion": 1,
                "telefono": 1,
                "_id": 0
            }
        )

    except Exception as e:
        raise Exception(str(e))


def handler(event, context):
    return list(find())
