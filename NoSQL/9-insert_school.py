#!/usr/bin/env python3
"""
Docstring pour NoSQL.9-insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    Docstring pour insert_school

    :param mongo_collection: Mongo collection
    :param kwargs: Datas as a dict
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
