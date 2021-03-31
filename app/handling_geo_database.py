from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.geolocation_service
collection_vehicle_mileage = db.mileage
collection_vehicle_stops = db.stops


class VehicleMileageCollection(object):

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
            collection_vehicle_mileage.insert_one({
                    self.mileage_km: item[10], self.time_en_route: item[11], self.downtime: item[12],
                    self.average_speed: item[13], self.max_speed: item[14], self.departure_time: item[15],
                    self.arrival_time: item[16]
                    })
        except IndexError:
            return False


class VehicleStopsCollection(object):

    def __init__(self, start_of_parking: str = 'start_of_parking', end_of_parking: str = 'end_of_parking',
                 time_of_stay: str = 'time_of_stay', starting_mileage: float = 'starting_mileage',
                 ending_mileage: float = 'ending_mileage', address: str = 'address'):
        self.start_of_parking = start_of_parking
        self.end_of_parking = end_of_parking
        self.time_of_stay = time_of_stay
        self.starting_mileage = starting_mileage
        self.ending_mileage = ending_mileage
        self.address = address

    def insert_to_collection(self, start_of_parking, end_of_parking, time_of_stay, starting_mileage, ending_mileage, address):
        try:
            collection_vehicle_stops.insert_one({
                    self.start_of_parking: start_of_parking,
                    self.end_of_parking: end_of_parking,
                    self.time_of_stay: time_of_stay,
                    self.starting_mileage: starting_mileage,
                    self.ending_mileage: ending_mileage,
                    self.address: address
                    })
        except IndexError:
            return False

    @staticmethod
    def size_collection():
        cursor = collection_vehicle_stops.find({}, {'_id': 0})
        for document in cursor:
            size_rows = len(document['time_of_stay'])
            return size_rows



def trash_remove(c):
    remove = c.delete_many({})
    print(remove.deleted_count, " documents deleted.")


