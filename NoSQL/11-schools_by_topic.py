#!/usr/bin/env python3
"""
Docstring pour NoSQL.11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Docstring pour schools_by_topic

    :param mongo_collection: Mongo collection
    :param topic: string your are looking for
    in the attribute
    """
    documents = mongo_collection.find({'topic': {'$in': [topic]}})
    return documents
