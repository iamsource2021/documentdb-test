import json
import os
import pymongo
import clientmongodb

from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()


def find_one(search):
    try:
        client = clientmongodb.client_mongo(
            os.environ['MONGODB_CLOUD_DEFAULT'])
        db = client['test']
        profiles = db['profiles']
        cursor = profiles.find(
            {"rfc": search},
            {
                "nombre": 1,
                "razonsocial": 1,
                "rfc": 1,
                "direccion": 1,
                "telefono": 1,
                "_id": 0
            }
        )

        result =  list(cursor)
        if len(result) == 0:
            raise Exception("Not Found "+search)
        else:
            return result[0]
        
    except Exception as e:
        raise Exception(str(e))


def handler(event, context):
    listProfile = find_one(event['arguments']['rfc'])
    return listProfile
