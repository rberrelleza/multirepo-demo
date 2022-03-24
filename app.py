import os
from pymongo import MongoClient

def lambda_handler(event, context):
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    database = os.getenv('MONGODB_DATABASE')
    client = MongoClient('mongodb+srv://' + username + ':' + password + '@mongodb-serverless.tussl.mongodb.net/' + database + '?retryWrites=true&w=majority')
    db = client['okteto']
    coll = db['votes']
    coll.insert_one(event)
    return ""
