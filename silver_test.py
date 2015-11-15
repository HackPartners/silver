from silverraw import silvershop, silvercom, silverbook, silvercore
from silver import SilverCore, Passenger, TravelPoint, FareSearch, FARE_FILTER
import pyxb
from datetime import datetime

sc = SilverCore("HackTrain", "GB", "CH2", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.nokey.pem", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.key")

p1 = Passenger(age=30)
p2 = Passenger(age=15)

tp1 = TravelPoint(
    origin="GBQQU", 
    destination="GBQQM",
    departure=datetime(2015, 11, 16, 12))

fq = FareSearch(
        travel_points = [tp1],
        fare_filter = FARE_FILTER.CHEAPEST,
        passengers = [p1, p2],
        specs = [
            "reservations",
            "accommodations",
            "onboardServices",
            "localServices",        
        ])

fares_result = sc.search_fare(fq)

print fares_result
