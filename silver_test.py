from silverraw import silvershop, silvercom, silverbook, silvercore
from silver import *
import pyxb
from datetime import datetime

cert = "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.nokey.pem"
key = "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.key"
sc = SilverCore("HackTrain", "GB", "CH2", cert, key)

# =======================================================
# ===================== Fares query =====================
# =======================================================

p1 = Passenger(age=30)

tp1 = TravelPoint(
    origin="GBQQU", 
    destination="GBQQM",
    departure=datetime(2015, 11, 16, 12))

fq = FareSearch(
        travel_points = [tp1],
        fare_filter = FARE_FILTER.CHEAPEST,
        passengers = [p1])

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
# ============= Booking From Fares Found ================
# =======================================================

p1 = Passenger(
    id="PAX_SPEC_0",
    age=30,
    first_name="Jane",
    last_name="Smith")

p1.add_contact(ContactInfo(CONTACT_TYPE.UNKNOWN, CONTACT_MEDIUM.PHONE, "123456789"))
p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.PHONE, "123456789"))
p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.EMAIL, "jsmith@email.com"))

passengers_chosen = [p1]

# Chose the legs for the journey
legs = [fares_result.results.legs.leg[0].legSolutions.legSolution[0]]

# Select fares chosen
fares = [fares_result.results.fareInformation.prices.pointToPointPrice[0]]

# Select passengers for the booking
passengers = [p1]

# Run booking request
booking_result = sc.create_booking_from_response(legs, fares, passengers)

print booking_result.toxml()

# =======================================================
# =============== Booking From Python ===================
# =======================================================


p1 = Passenger(
    id="PAX_SPEC_0",
    age=40,
    first_name="Jane",
    last_name="Smith")

p1.add_contact(ContactInfo(CONTACT_TYPE.UNKNOWN, CONTACT_MEDIUM.PHONE, "123456789"))
p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.PHONE, "123456789"))
p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.EMAIL, "jsmith@email.com"))

ts1 = TravelSegment(
        id = "LS_1_1_TS_0", 
        sequence = 0,
        origin = "GBRDG",
        destination = "GBQQM",
        departure = "2015-12-07T06:15:00",
        arrival = "2015-12-07T09:38:00",
        designator = "XC3040",
        marketing_carrier = "CrossCountry",
        operating_carrier = "CrossCountry",
        equipment_type = "ICY",
        equipment_type_str = "Inter-City")

leg1 = Leg(
    id="LS_1_1",
    travel_segments=[ts1])

fc1 = FareCode(
    code="IXC-FOS-00700-STD-1",
    service_class="FIRST",
    travel_segment_id = "LS_1_1_TS_0",
    cabin_class="First",
    fare_display_name="Anytime Single (1st Class)")

# Creating passenger reference with one fare code (As there is 1 travel segment)
pr1 = PassengerReference(p1, PASSENGER_TYPE.A, [fc1])

# The FarePrice breakdown for the total ticketable fare cost 
price1 = FarePrice(319.52, "TICKET", "USD")

tf1 = TicketableFare(
        price= 319.52,
        prices = [price1],
        currency="GBP",
        passenger_references=[pr1])

f1 = FareTotal(
        id = "PRICE_P_1_23", 
        currency = "GBP", 
        price = 319.52, 
        expiration = "2015-10-27T15:50:33Z",
        ticketable_fares = [tf1],
        legs = [leg1])

fares = [f1]
passengers = [p1]

# Run booking request
booking_result = sc.create_booking(fares, passengers)

# View results

print booking_result.requestStatus.success # True

print booking_result.recordLocator # B-HACKTRAIN-IKS000262
print booking_result.lastHoldDateTime # 2015-11-15T15:49:09Z

# Store record locator to add payment, add ticket option, and confirm booking
# See the other examples for this
record_locator = booking_result.recordLocator


# =======================================================
# ==================== Add Payment ======================
# =======================================================


b = BillingAddress(
        address1="9 Broad Court, Long Acre",
        city="London",
        zip_code="WC2B 5QN",
        country="GB",
        type=ADDRESS_TYPE.BUSINESS)

p = PaymentMethod(
    record_locator=record_locator,
    payment_form="CA",
    payment_form_type=PAYMENT_TYPE.CREDIT_CARD,
    card_number="5425232820001308",
    card_type="CA",
    card_holder_first_name="Jane",
    card_holder_last_name="Smith",
    expiration_year=2016,
    expiration_month=12,
    card_validation_number="123",
    amount=198.20,
    currency="GBP",
    customer_ip_address="1.1.1.1",
    billing_address=b)

payment_response = sc.add_payment(p)

print payment_response.requestStatus.success # True
print payment_response.paymentToken # Nl6qpzWfQiylKDaExw2W/g==

payment_token = payment_response.paymentToken


# =======================================================
# ==================== Add Delivery =====================
# =======================================================

to1 = TicketOption(
    TICKET_DELIVERY_OPTION.VENDING_MACHINE,
    "GBP",
    0.00)

bu = BookingUpdate(
                record_locator=record_locator,
                ticket_option=to1)

booking_update = sc.update_booking(bu)

print booking_update.requestStatus.success # True

# =======================================================
# =================== Confirm Booking ===================
# =======================================================


b = BookingConfirmation(
    record_locator=record_locator,
    confirmation_type=CONFIRMATION_TYPE.CREDIT_CARD,
    card_number="5425232820001308",
    expiration_year=2016,
    expiration_month=12,
    card_holder_first_name="Jonathan",
    card_holder_last_name="Harrah")

booking_confirm = sc.confirm_booking(b)

print booking_confirm.requestStatus.success # True










