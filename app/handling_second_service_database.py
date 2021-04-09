from datetime import datetime, timedelta
import pdfplumber
import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.second_service
collection_rides = db.rides
collection_payments = db.payments


class SecondServiceDatabase(object):

    def __init__(self):
        self.file_rides = f"/home/oleg/python/geolocation_service/new_file_{datetime.now().strftime('%H_%M')}.csv"
        self.file_rides = f"/dev/shm/new_file_{datetime.now().strftime('%H_%M')}.csv"
        #self.file_payments = f"/home/oleg/python/geolocation_service/new_file_{datetime.now().strftime('%H_%M')}.pdf"

    def insert_document_to_rides_collection(self):
        try:
            self.trash_remove(collection_rides)
            with open(self.file_rides) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        collection_rides.insert_one({'order_time': row[0], 'landing_address': row[1], 'cost': row[2],
                                                     'authorization_payment': row[3], 'fees_charged': row[4],
                                                     'cancellation_fee': row[5],
                                                     'bonus': row[6], 'currency': row[7], 'payment_method': row[8],
                                                     'time_payment': row[9], 'distance': row[10], 'status': row[11]})
                        line_count += 1
                    else:
                        collection_rides.insert_one({'order_time': row[0], 'landing_address': row[1], 'cost': row[2],
                                                     'authorization_payment': row[3], 'fees_charged': row[4],
                                                     'cancellation_fee': row[5],
                                                     'bonus': row[6], 'currency': row[7], 'payment_method': row[8],
                                                     'time_payment': row[9], 'distance': row[10], 'status': row[11]})
                        line_count += 1
                print(f'Processed {line_count} lines.')
        except IndexError:
            return False

    def insert_document_to_payments_collection(self):
        try:
            self.trash_remove(collection_payments)
            with pdfplumber.open(self.file_payments) as pdf:
                first_page = pdf.pages[0].extract_text(x_tolerance=3, y_tolerance=3)

            total_cost = first_page[62:66]
            commission = first_page[83:88]
            total_cash = first_page[110:113]
            balance = first_page[131:136]

            collection_payments.insert_one({'total_cost': total_cost, 'commission': commission, 'total_cash': total_cash, 'balance': balance})
        except IndexError:
            return False

    @staticmethod
    def trash_remove(c):
        remove = c.delete_many({})
        print(remove.deleted_count, " documents deleted.")


    @staticmethod
    def check_transfer_funds():
        with open("/home/oleg/python/geolocation_service/acquiring.csv") as file:
            reader = csv.reader(file, delimiter=',')
            line = 0
            for item in reader:
                if line == 0:
                    for i in item:
                        result = i.replace(' ', '')
                line += 1
        acquiring = float(result[0:5])

        collection = collection_payments.find()
        balance = None
        for obj in collection:
            balance = obj['balance']
        on_balance = float(balance)
        return acquiring == on_balance


    def check_total_amount(self):
        """ use this method last work day of week """
        query_order = collection_rides.find().skip(1)
        arr = []
        start = datetime.now()
        date = start - timedelta(days=7)
        from_date = date.strftime("%d.%m.%Y")
        first_day = [cost['order_time'] for cost in query_order if (cost['order_time'].startswith(from_date))]
        for cost in collection_rides.find().skip(1):
            total_cost = cost['cost'], cost['order_time']
            if total_cost[1] == first_day[0]:
                arr.append(int(cost['cost']))

            if total_cost[1] == first_day[1]:
                arr.append(int(cost['cost']))

        for cost in collection_rides.find().skip(1):
            if cost['order_time'].startswith(from_date):
                break

            arr.append(int(cost['cost']))

        result = 0
        for item in arr:
            result += item

        with pdfplumber.open(self.file_payments) as pdf:
            first_page = pdf.pages[0].extract_text(x_tolerance=3, y_tolerance=3)
        total_payment = first_page[62:66]

        return total_payment == result



