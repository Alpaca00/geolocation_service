from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client.second_service
collection_admin = db.admin



class Employee:

    @property
    def find_email(self):
        query = collection_admin.find({'_id': ObjectId('60684f422eea8521c337072e')}, {'_id': 0})
        for item in query:
            return item['email']

    @property
    def find_password(self):
        query = collection_admin.find({'_id': ObjectId('60684f612eea8521c337072f')}, {'_id': 0})
        for item in query:
            return item['password']

    @property
    def find_main_page_title(self):
        query = collection_admin.find({'_id': ObjectId('60695e84b4e6808bf0c07efa')}, {'_id': 0})
        for item in query:
            return item['home_title']

    @property
    def find_rides_page_title(self):
        query = collection_admin.find({'_id': ObjectId('60696700b4e6808bf0c07efb')}, {'_id': 0})
        for item in query:
            return item['rides_title']

    @property
    def find_bills_page_title(self):
        query = collection_admin.find({'_id': ObjectId('60697419b4e6808bf0c07efc')}, {'_id': 0})
        for item in query:
            return item['bills_title']

    @property
    def find_compensation_page_title(self):
        query = collection_admin.find({'_id': ObjectId('60697c2db4e6808bf0c07efd')}, {'_id': 0})
        for item in query:
            return item['compensation_title']

    @property
    def find_condition_text_for_compensation_page(self):
        query = collection_admin.find({'_id': ObjectId('606981c5b4e6808bf0c07efe')}, {'_id': 0})
        for item in query:
            return item['condition']

    @property
    def find_payments_page_title(self):
        query = collection_admin.find({'_id': ObjectId('60698983b4e6808bf0c07eff')}, {'_id': 0})
        for item in query:
            return item['payments_title']

    @property
    def find_acquiring_page_title(self):
        query = collection_admin.find({'_id': ObjectId('606abd2ca4d1383cb4d2c2e3')}, {'_id': 0})
        for item in query:
            return item['acquiring_title']

    @property
    def token(self):
        query = collection_admin.find({'_id': ObjectId('606ac374a4d1383cb4d2c2e4')}, {'_id': 0})
        for item in query:
            return item['token']
