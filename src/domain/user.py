from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client.geolocation_service
collection_admin = db.admin



class User(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.admin = Admin()

    def get_admin_username(self):
        for value in self.admin.username_query:
            return value['username']

    def get_admin_password(self):
        for value in self.admin.password_query:
            return value['password']


class Admin(object):
    logo_query = collection_admin.find({'_id': ObjectId('6059fd52af04b3d20b3078a2')}, {'_id': 0})
    logo_mileage_page = collection_admin.find({'_id': ObjectId('605b8695ad9c79d41d139f4e')}, {'_id': 0})

    def __init__(self):
        self.username_query = collection_admin.find({'_id': ObjectId('6059db7ae8e6d81068caf50d')}, {'_id': 0})
        self.password_query = collection_admin.find({'_id': ObjectId('6059dba7e8e6d81068caf50e')}, {'_id': 0})

    def main_logo(self):
        for value in self.logo_query:
            return value['logo']

    def mileage_logo(self):
        for value in self.logo_query:
            return value['logo_mileage_page']
