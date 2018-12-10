import os

from pymongo import MongoClient

client = MongoClient('db_mongo_iot', 27018, username=os.environ['MONGO_INITDB_ROOT_USERNAME'],
                     password=os.environ['MONGO_INITDB_ROOT_PASSWORD'])

collection_name = 'data_from_device'


def insert_document(document, collection=collection_name):
    document_obj = client[collection]
    return document_obj.insert_one(document).inserted_id


def get_document_by_id(document_id, collection=collection_name):
    document_obj = client[collection]
    filter = {'id_': document_id}
    document_result = document_obj.find(filter)
    return list(document_result)


def get_all(collection=collection_name):
    document_obj = client[collection]
    documents = document_obj.find()
    return list(documents)
