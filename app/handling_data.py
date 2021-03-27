from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.geolocation_service
collection_mileage = db.mileage


class MileageCollection(object):

    def __init__(self, mileage_km: str = 'mileage_km', time_en_route: str = 'time_en_route', downtime: str = 'downtime',
                 average_speed: str = 'average_speed', max_speed: str = 'max_speed',
                 departure_time: str = 'departure_time', arrival_time: str = 'arrival_time'):
        self.mileage_km = mileage_km
        self.time_en_route = time_en_route
        self.downtime = downtime
        self.average_speed = average_speed
        self.max_speed = max_speed
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def insert_to_collection(self, item):
        try:
            collection_mileage.insert_one({
                    self.mileage_km: item[10], self.time_en_route: item[11], self.downtime: item[12],
                    self.average_speed: item[13], self.max_speed: item[14], self.departure_time: item[15],
                    self.arrival_time: item[16]
                    })
        except IndexError:
            return False
