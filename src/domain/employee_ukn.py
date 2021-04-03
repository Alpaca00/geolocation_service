from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client.geolocation_service
collection_admin = db.admin


class Admin(object):

    @property
    def find_license_plate(self):
        query = collection_admin.find({'_id': ObjectId('6064b1a3b3a9ff882c31652c')}, {'_id': 0})
        for item in query:
            return item['license_plate']

    @property
    def find_email_ukn(self):
        query = collection_admin.find({'_id': ObjectId('6064b799b3a9ff882c31652e')}, {'_id': 0})
        for item in query:
            return item['email_ukn']

    @property
    def find_password_ukn(self):
        query = collection_admin.find({'_id': ObjectId('6064b7bbb3a9ff882c31652f')}, {'_id': 0})
        for item in query:
            return item['password_ukn']


class Employee(Admin):
    def __init__(self, id):
        super(Employee).__init__()
        self.id = id

    def __str__(self):
        return self.id

    def change_id(self, new_id):
        self.id = new_id
        return f'{self.id}'

    @property
    def format_start_date_for_payments(self):
        start = datetime.now()
        result_date = start - timedelta(days=7)
        return result_date.strftime("%d.%m.%Y 00:00")

    @property
    def format_end_date_for_payments(self):
        return datetime.now().strftime("%d.%m.%Y 00:00")

    @property
    def format_start_date_for_rides(self):
        start = datetime.now()
        date = start - timedelta(days=7)
        result = date.strftime("%m/%d/%Y")
        return f"{result}, 3:00 AM"

    @property
    def format_end_date_for_rides(self):
        result = datetime.now().strftime("%m/%d/%Y")
        return f"{result}, 3:00 AM"


