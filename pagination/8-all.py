#!/usr/bin/env python3
"""
Docstring pour pagination.8-all
"""


def list_all(mongo_collection):
    """
    Docstring pour list_all

    :param mongo_collection: a mongo
    collection
    """
    documents = mongo_collection.find()
    return documents
