#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    logs = logs_collection.find()
    print(f'{logs.count_documents({})} logs')
    print("Methods")
    get = logs_collection.find({'method': 'GET'})
    post = logs_collection.find({'method': 'POST'})
    put = logs_collection.find({'method': 'PUT'})
    patch = logs_collection.find({'method': 'PATCH'})
    delete = logs_collection.find({'method': 'DELETE'})
    status = logs_collection.find({'method': 'GET', 'path': '/stats'})
    print("\t" + "method GET: " + len(get.count_documents({})))
    print("\t" + "method POST: " + len(post.count_documents({})))
    print("\t" + "method PUT: " + len(put.count_documents({})))
    print("\t" + "method PATCH: " + len(patch.count_documents({})))
    print("\t" + "method DELETE: " + len(delete.count_documents({})))
    print(f'{status.count_documents({})} status check')
