import os
from pymongo import MongoClient

def lambda_handler(event, context):
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    database = os.getenv('MONGODB_DATABASE')
    client = MongoClient('mongodb', username=username, password=password, authSource=database, port=27017)
    db = client['okteto']
    coll = db['votes']
    coll.insert_one(event)
    return ""


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def vote():
    request_data = request.get_json()



if __name__ == '__main__':
  print('Starting lambda server...')
  app.run(host='0.0.0.0', port=8080)