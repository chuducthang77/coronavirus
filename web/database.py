from pymongo import MongoClient
import json

def insert(data, collection):
    collection.insert_many(data)

def main():
    client = MongoClient('mongodb://localhost:27012')

    db = client['Covid']

    myGisaid = db['gisaid']
    with open('db.json') as f:
        myList = json.load(f)
    
    insert(myList, myGisaid)

    cursor = myGisaid.find_one()
    for x in cursor:
        print(x)

if __name__ == "__main__":
    main()