#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    logs = logs_collection.find()
    print(f'{logs.count()} logs')
    print("Methods")
    get = logs_collection.find({'method': 'GET'})
    post = logs_collection.find({'method': 'POST'})
    put = logs_collection.find({'method': 'PUT'})
    patch = logs_collection.find({'method': 'PATCH'})
    delete = logs_collection.find({'method': 'DELETE'})
    status = logs_collection.find({'method': 'GET', 'path': '/stats'})
    print("\t" + "method GET: " + len(get.count()))
    print("\t" + "method POST: " + len(post.count()))
    print("\t" + "method PUT: " + len(put.count()))
    print("\t" + "method PATCH: " + len(patch.count()))
    print("\t" + "method DELETE: " + len(delete.count()))
    print(f'{status.count()} status check')
