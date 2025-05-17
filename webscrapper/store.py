from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["website-data"]
collection = db["websites"]

def save_to_mongo(data, category):
    if data:
        data['category'] = category
        data['timestamp'] = datetime.utcnow()
        collection.insert_one(data)
        print(f"Saved {data['url']} to MongoDB")
    else:
        print("No data to save")
