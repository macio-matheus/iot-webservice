import os

from pymongo import MongoClient

cliente = MongoClient('db_mongo_iot', 27018, username=os.environ['MONGO_INITDB_ROOT_USERNAME'],
                      password=os.environ['MONGO_INITDB_ROOT_PASSWORD'])

collection_name = 'data_from_device'


def insert_document(self, document, collection=collection_name):
    document_obj = self.database[collection]
    return document_obj.insert_one(document).inserted_id


def get_document_by_id(self, document_id, collection=collection_name):
    document_obj = self.database[collection]
    filter = {'id_': document_id}
    document_result = document_obj.find(filter)
    return list(document_result)


def get_all(self, collection=collection_name):
    docdocument_obj = self.database[collection]
    documents = docdocument_obj.find()
    return list(documents)
