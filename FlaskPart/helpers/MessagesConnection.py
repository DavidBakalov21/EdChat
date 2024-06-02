from pymongo import MongoClient
import certifi
def get_mongo_message_collection():
    try:
        client = MongoClient('MONGO CONNECTION STRING', tlsCAFile=certifi.where())
        db = client['Chat']
        collection = db['RoomMessagesFlask']
        return collection
    except Exception as e:
        print("can't reach mongo")
        return None