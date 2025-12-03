#!/usr/bin/env python3
"""
Docstring pour NoSQL.10-update_topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Docstring pour update_topics

    :param mongo_collection: Mong collection
    :param name: name to use to filter datas
    :param topics: attribute values to modify/create
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}})
