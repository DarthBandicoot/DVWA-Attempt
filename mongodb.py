import pymongo

_author_ = "lewis"

uri = "mongodb://Lewis:starwars10@192.168.0.119/dvwa"
client = pymongo.MongoClient(uri)
database = client['dvwa']
collection = database['users']


def save_user_record():
    pass
