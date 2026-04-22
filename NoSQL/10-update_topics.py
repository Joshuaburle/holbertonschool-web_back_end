#!/usr/bin/env python3
"""Update topics of a school"""


def update_topics(mongo_collection, name, topics):
    """Updates all documents with a given name by setting topics"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
