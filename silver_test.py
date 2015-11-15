from silverraw import silvershop, silvercom, silverbook, silvercore
from silver import SilverCore, Passenger, TravelPoint, FareSearch, FARE_FILTER, CONTACT_TYPE, FareTotal, TravelSegment
import pyxb
from datetime import datetime

sc = SilverCore("HackTrain", "GB", "CH2", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.nokey.pem", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.key")

# =======================================================
# ===================== Fares query =====================
# =======================================================

p1 = Passenger(age=30)
p2 = Passenger(age=15)

tp1 = TravelPoint(
    origin="GBQQU", 
    destination="GBQQM",
    departure=datetime(2015, 11, 16, 12))

fq = FareSearch(
        travel_points = [tp1],
        fare_filter = FARE_FILTER.CHEAPEST,
        passengers = [p1, p2])

fares_result = sc.search_fare(fq)

print fares_result.requestStatus
print fares_result.requestStatus.success

fr = fares_result.results

for l in fr.legs.leg:
    print l.originTravelPoint.value()
    print l.originTravelPoint.type
    print l.destinationTravelPoint.value()
    print l.destinationTravelPoint.type

    for p in fr.passengers.passenger:
        print p.passengerSpecID
        print p.age

    for s in l.legSolutions.legSolution:
        print s.legSolutionID
        print s.overtakenJourney
        print s.duration

        for a in s.availableSeatPreferences.availableSeatPreference:
            print a.marketingCarrier
            print a.serviceClass
            print a.supplierEquipmentType
            print a.value()

        for r in s.passengerInformationRequired.passengerInformation:
            print r.type
            print r.allPassengers

        for t in s.travelSegments.travelSegment:
            print t.sequence
            print t.travelSegmentID
            print t.originTravelPoint.type
            print t.originTravelPoint.value()
            print t.destinationTravelPoint.type
            print t.destinationTravelPoint.value()
            print t.arrivalDateTime
            print t.designator
            print t.operatingCarrier.value()
            print t.supplierEquipmentType.value()
            print t.duration
            print t.crossBorderInfo
            print t.equipmentType.code
            print t.equipmentType.value()
            print t.marketingServiceName
            print t.marketingInformation.serviceCode

    for p in fr.fareInformation.prices.pointToPointPrice:
        print p.priceID
        print p.totalPrice.currency
        print p.totalPrice.value()
        print p.holdExpiration
        
        for l in p.legReferences.legSolutionIDRef:
            print l

        for t in p.ticketableFares.ticketableFare:
            print t.totalPrice
            print t.totalPrice.currency
            print t.totalPrice.value()
            print t.ticketingOptionsAvailable.TOD
            print t.ticketingOptionsAvailable.ETK
            print t.ticketingOptionsAvailable.PAH
            print t.ticketingOptionsAvailable.EML
            print t.ticketingOptionsAvailable.DEPARTURE_STATION_TOD
            print t.ticketingOptionsAvailable.SMS
            print t.fareOrigin.type
            print t.fareOrigin.value()
            print t.fareDestination.type
            print t.fareDestination.value()

            if t.fareDestinationTerminals:
                for d in t.fareDestinationTerminals.fareDestinationTerminal:
                    print d.type
                    print d.value()

            for r in t.passengerReferences.passengerReference:
                print r.passengerIDRef
                print r.passengerTypeCode

                for c in r.fareCodes.fareCode:
                    print c.code
                    print c.serviceClass
                    print c.travelSegmentIDRef
                    print c.cabinClass
                    print c.rewardsEligible
                    print c.fareClass
                    print c.fareDisplayName
                    print c.openReturn
                    print c.reservable
                    print c.fareExpirationDateTime

                    for a in c.amenities.amenity:
                        print a.type
                        print a.value()

                    for f in c.fareApplicabilities.fareApplicability:
                        print f.outbound
                        print f.type
            
            for r in t.prices.price:
                print r.type
                print r.currency
                print r.value()

            for o in t.optionalPrices.optionalPrice:
                # TODO: Add consumption rules
                print o.optionalPriceID
                print o.category
                print o.applicableTravelSegments.travelSegmentIDRef
                print o.maximumBookableQuantity

                for u in o.rules.rule:
                    print u.type
                    print u.priceType
                    print u.applicableOrderStatus
                    print u.refundToVoucher

            for c in t.commissions.commission:
                print c.type
                print c.currency
                print c.value()

            for r in t.rules.rule:
                print r.type
                print r.description
                print r.priceType
                print r.applicableOrderStatus

                if r.penalty:
                    print r.penalty.currency
                    print r.penalty.value()



# =======================================================
# ======================= Booking =======================
# =======================================================

p1 = Passenger(
    passenger_id="PAX_SPEC_0",
    age=30,
    first_name="Jane",
    last_name="Smith",
    passenger_type=PASSENGER_TYPE.C)

p1.add_contact(ContactInfo(CONTACT_TYPE.HOME, CONTACT_MEDIUM.PHONE, "123456789"))
p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.EMAIL, "lol@hack.com"))

ts1 = TravelSegment(
        id = "LS_1_2_TS_0", 
        sequence = 0,
        origin = "GBRDG",
        destination = "GBQQP",
        departure = "2015-12-07T10:07:00",
        arrival = "2015-12-07T10:37:00",
        designator = "GW4205",
        marketing_carrier = "FirstGrtWest",
        operating_carrier = "FirstGrtWest",
        equipment_type = "ICY",
        equipment_type_str = "Inter-City")

leg1 = Leg(
    id="LS_1_2",
    travel_segments=[ts1])

fc1 = FareCode(
    code="IWC-SOS-00200-STD-1",
    service_class="THIRD",
    travel_segment_id = "LS_1_2_TS_1",
    cabin_class="Standard",
    fare_display_name="Anytime Single")

tf1 = TicketableFare(
        price= 48.50,
        currency="GBP",
        fare_codes=[fc1],
        passengers=[p1])

f1 = FareTotal(
        id = "PRICE_P_1_23", 
        currency = "GBP", 
        price = 48.50, 
        expiration = "2015-10-27T15:50:33Z",
        ticketable_fares = [tf1],
        legs = [leg1])

fares = [f1]
passengers = [p1]

# Run booking request
booking_result = sc.create_booking(fares, passengers)
