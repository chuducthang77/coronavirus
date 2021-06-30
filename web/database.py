from pymongo import MongoClient
import json

def insert(data, collection):
    collection.insert_many(data)

def main():
    client = MongoClient('mongodb+srv://user:772000@cluster0.ntvp9.mongodb.net/coronavirus?retryWrites=true&w=majority')

    db = client['covid']

    myGisaid = db['refs']
    with open('ref.json') as f:
        myList = json.load(f)
    
    insert(myList, myGisaid)

    # cursor = myGisaid.find_one()
    # for x in cursor:
    #     print(x)

if __name__ == "__main__":
    main()