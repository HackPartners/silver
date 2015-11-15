from silvercore import *

# Initialize with disrtibutor, point of sale, and channel
sc = silver.SilverCore("HackTrain", "GB", "CH2", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.nokey.pem", "/Users/bloomberglondonrd1/.ssh/certificates/hacktrain.key")

# =======================================================
# ===================== Fares query =====================
# =======================================================

tp1 = TravelPoint(
    origin="GBQQU", 
    destination="GBQQM")

tp2 = TravelPoint(
    origin="GBQQM", 
    destination="GBQQU", 
    departure=datetime(2015, 12, 04, 9), 
    arrival=datetime(2015, 12, 04, 12))

p1 = Passenger(age=30)
p2 = Passenger(age=15)

fq = FareSearch(
        travel_points = [tp1, tp2],
        fare_filter = FARE_FILTER.CHEAPEST,
        passengers = [p1, p2],
        specs = [
            "reservations",
            "accommodations",
            "onboardServices",
            "localServices",        
        ])

print fq.passengers[0].id # "PAX_SPEC_0"
print fq.passengers[1].id # "PAX_SPEC_1"

# Run the query
fares_result = sc.search_fare(fq)

# See results
print fares_result.success # True

for p in fares_result.passengers:
    print p.id # "PAX_SPEC_0"
    print p.age # 30

for l in fares_result.legs:
    print l.id # LS_1_0
    print l.overtaken # False -- whether there is another solution faster
    print l.duration
    print l.passenger_info_req # [PASSENGER_ADDRESS, TRAVEL_DOCUMENTS, ...]

    for s in l.available_seats:
        print s.marketing_carrier # Virgin
        print s.service_class # FIRST
        print s.supplier_equipment # Virgin-ICY
        print s.type # AISLE

    for t in l.travel_segments:
        print t.id # TS-SIX000255-ZBI000001-1
        print t.type # TRAIN
        print t.leg_grouping # 1
        print t.origin # GBQQU
        print t.destination # GBQQM
        print t.departure # datetime(2015, 12, 04, 9, 45)
        print t.arrival # datetime(2015, 12, 04, 12, 30)
        print t.designator # VT7050 -- Train number
        print t.marketing_carrier # Virgin
        print t.operating_carrier # Virgin
        print t.duration # P0Y0M0DT2H8M0S
        print t.cross_border # False -- Whether we cross border
        print t.equipment_code # HSP

    for f in l.fares:    
        print f.id # PRICE_LS_1_1_0
        print f.currency # GBP
        print f.amount # 246
        print f.hold_expiration # 2015-10-19T20:05:29Z

        for p in l.prices:
            print p.type # TICKET
            print p.currency # GBP
            print p.amount # 164.50

        for op in l.optional_prices:
            print p.type # TICKET
            print p.currency # GBP
            print p.amount # 164.50
            print p.applicable_segments # ["LS_1_0_TS_0", ...]

            for r in op.rules:
                print r.type # EXCHANGE_PROHIBITED
                print r.price_type # TICKET
                print r.applicable_order_status # BOOKED
                print r.refund_to_voucher # NOT_POSSIBLE


        for pf in l.passenger_references:
            print pf.passenger_id # PAX_SPEC_1
            print pf.passenger_category # C -- Age category
            print pf.amount # 82.25
            print pf.currency # GBP
            print pf.origin # GBLNT
            print pf.destination # GBMPV

            c = pf.commission
            print c.type # DISTRIBUTOR
            print c.currency #GBP
            print c.amount # 4.32

            t = pf.ticketing_options_available
            print t.ticket_on_departure # True
            print t.e_ticket # False
            print t.print_at_home # False
            print t.sms # False
            print t.departure_station_tod # True

            for r in pf.rules:
                # Same as rules above
                pass

            for fc in pf.fare_codes:
                print fc.code # IWC-SOS-00000-STD-1
                print fc.service_class # THIRD
                print fc.segment # LS_1_0_TS_0
                print fc.cabin_class # Standard
                print fc.rewards_elegible # False
                print fc.fare_class # ANYTIME
                print fc.display_name # Anytime Single
                print fc.open_return # False
                print fc.reservable # OPTIONAL
                print fc.expiration # 2015-12-06T02:30:00Z

                for a in fc.amenities:
                    print a.type # INTERNET_AVAILABLE
                    print a.printable # WiFi access (Additional Cost)

                for a in fc.applicabilities:
                    print a.outbound # OPEN
                    print a.return_leg # None
                    print a.type # SCHEDULE


# =======================================================
# ======================= Booking =======================
# =======================================================

# Choose a fare per leg

t1 = TravelSegment(
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

f1 = FareTotal(
        id: = "PRICE_P_1_23", 
        currency = "GBP", 
        total_amount = 48.50, 
        leg_id = "LS_1_2", 
        expiration = "2015-10-27T15:50:33Z",
        segments = [t1]
        parameters = [FARE_PARAMS.ACCEPT_ANY],
        specs = [FARE_SPECS.RETURN_DETAILS])

p1 = Passenger(
    passenger_id="PAX_SPEC_0",
    age=30)

p2 = Passenger(
    passenger_id="PAX_SPEC_1",
    age=15)

p1.add_contact(CONTACT_TYPE.HOME, CONTACT_MEDIUM.PHONE, "123456789")
p1.add_contact(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.EMAIL, "lol@hack.com")
p2.add_contact(CONTACT_TYPE.UNKNOWN, CONTACT_MEDIUM.PHONE, "lol@lol.co")

fares_chosen = [f1]
passengers = [p1,p2]

# Run booking request
booking_result = sc.create_booking(fares_chosen, passengers)


# Read booking response

print booking_result.success # True
print booking_result.system_id # C5OTaN
print booking_result.record_locator # B-DEMO-OSV000254
print booking_result.last_holding # 2015-11-13T23:37:04Z
print booking_result.updateable # ["passengerIdentity", "passengerAddress", "passengerContactInfo", ...]
print booking_result.booking_date # 2015-11-14Z
print booking_result.departure_date # 2015-12-07
print booking_result.number_of_orders # 1
print booking_result.revenue_total # 544.30
print booking_result.revenue_currency # GBP
print booking_result.recipts_total # 0.00
print booking_result.recipts_currency # GBP

for p in booking_result.passengers:
    print p.first_name
    print p.last_name

    for c in p.contact_information:
        print c.id # P-SIX000255-1
        print c.type # UNKNOWN
        print c.medium # PHONE
        print c.info # 123456890

for o in booking_result.orders:
    print o.id # O-DEMO-SIX000255-ZBI000001
    print o.status # BOOKED
    print o.booking_date # 2015-11-14Z
    print o.hold_expiration # 2015-11-14T13:01:55Z
    print o.refund_elegibility # True
    print o.cancel_required_for_refund # True
    print o.penalty_amount # 0.00
    print o.penalty_currency # GBP
    print o.cancellable # True
    print o.partially_cancellable # True
    print o.price_reversal_amount # 544.30
    print o.price_reversal_currency # GBP
    print o.ticket_languages # ["en", "es", ...]
    print o.amount # 96.50
    print o.currency # GBP
    print o.confirmation_info_required # False
    print o.payment_required_for_confirmation # False
    print o.credit_card_options # ["AX", "CA", "DI", ...]
    print o.debit_card_options # ["MD", "VD", ...]
    print o.sort_code_required # False
    print o.commercial_agent_name # SilverRail Technologies UK Ltd - 3258

    pr = o.payment_requirements
    print pr.payment_due # 2015-11-14T13:01:55Z
    print pr.payment_information # ORDER_TOTAL
    print pr.next_deposit_due # 2015-11-14T13:01:55Z
    print pr.min_deposit_amount # 544.30
    print pr.min_deposit_currency # GBP
    print pr.refund_processed_on_cancel # False
    print pr.confirmation_upon_add_payment # False
    print pr.service_fee_allowed # True

    for p in o.order_prices:
        print p.id # FIN_PRICE_811
        print p.type # Product_Sale
        print p.ref # O-DEMO-SIX000255-ZBI000001
        print p.amount # 544.30
        print p.currency # GBP
        print p.posting_date # 2015-11-14Z

    for f in pr.payment_forms:
        print f.type # CC
        print f.form # AX

    for t in o.travel_segments:
        # Same as travel segments above
        pass

    for p in o.price_reversal_components:
        print p.type # Product_Sale
        print p.currency # GBP
        print p.amount # 544.30

    for c in o.cancellation_options:
        print c.refund_target # FORM_OF_PAYMENT
        print c.penalty_amount # 0.00
        print c.penalty_currency # GBP

    for f in o.fares:
        # Same as fares above
        pass

    for t in o.ticketing_options:
        print t.code # TBM
        print t.type # MAIL
        print t.destination # UK
        print t.description # Ticket by Royal Mail Special Delivery
        print t.refundable # False
        print t.currency # GBP
        print t.amount # 6.00

    for s in o.supply_channels:
        s.ref # P-SIX000255-2
        s.first_name # Joe
        s.last_name # Smith



# =======================================================
# ===================== Add Payment =====================
# =======================================================

b = BillingAddress(
        address1="9 Broad Court, Long Acre",
        city="London",
        zip_code="WC2B 5QN"
        country="GB",
        type="BUSINESS"
    )

p = PaymentMethod(
    record_locator="B-DEMO-WLC000133",
    payment_form="CA",
    payment_form_type="CC",
    card_number="5425232820001308",
    card_type="CA",
    card_holder_first_name="Jonathan",
    card_holder_last_name="Harrah",
    amount=31.20,
    currency="GBP",
    customer_ip_address="1.1.1.1",
    billing_address=b,
    response_spec=["returnReservationDetails"])

payment_response = sc.add_payment(p)

print payment_response.success # True
# Same booking record response as above



# =======================================================
# =================== Confirm Booking ===================
# =======================================================

 p = PaymentMethod(
    record_locator="B-DEMO-WLC000133",
    card_number="5425232820001308",
    card_holder_first_name="Jonathan",
    card_holder_last_name="Harrah",
    response_spec=["returnReservationDetails"])

 payment_response = sc.confirm_booking(p)






