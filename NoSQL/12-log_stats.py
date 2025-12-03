#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print(f'{logs_collection.count_documents({})} logs')
    print("Methods:")
    get = logs_collection.count_documents({'method': 'GET'})
    post = logs_collection.count_documents({'method': 'POST'})
    put = logs_collection.count_documents({'method': 'PUT'})
    patch = logs_collection.count_documents({'method': 'PATCH'})
    delete = logs_collection.count_documents({'method': 'DELETE'})
    status = logs_collection.count_documents(
        {'method': 'GET',
         'path': '/status'})
    print(f'\tmethod GET: {get}')
    print("\t" + "method POST: " + str(post))
    print("\t" + "method PUT: " + str(put))
    print("\t" + "method PATCH: " + str(patch))
    print("\t" + "method DELETE: " + str(delete))
    print(f'{status} status check')
