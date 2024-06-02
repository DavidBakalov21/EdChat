from pymongo import MongoClient
import certifi
def get_mongo_collection():
    try:
        client = MongoClient('MONGO CONNECTION STRING', tlsCAFile=certifi.where())
        db = client['Chat']
        collection = db['Accounts']
        return collection
    except Exception as e:
        print("can't reach mongo")
        return None  