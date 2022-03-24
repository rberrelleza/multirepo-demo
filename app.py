from pymongo import MongoClient


def lambda_handler(event, context):
    client = MongoClient('mongodb', username="okteto", password="okteto", authSource="okteto", port=27017)
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