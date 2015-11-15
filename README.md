# Silver.py: Rail payments made easy
#### The friendly open source SilverCore python interface

## What is silver.py?
A python wrapper for SilverRail's globally renowned SilverCore API. This python wrapper aims to provide a thin layer that abstracts the SOAP and SSL leg-work, and exposes a simple, pythonic interface. It's very simple to get started!

### Installing
``` bash
    pip install silver
```

### Initialize the SilverClient
In order to initialize the SilverClient, you will require:

* distributor (HackTrain)
* pointOfSale (GB)
* channel (CH1)
* SILVERCORE_CERT (Path to your SilverCore Certificate)
* SILVERCORE_KEY (Path to your SilverCore Key)

*Then just run the following commend*
``` python
    cert = os.environ("SILVERCORE_CERT")
    key = os.environ("SILVERCORE_KEY")
    sc = SilverCore("HackTrain", "GB", "CH2", cert, key)
```
    
### Search for available Fares
To start with, you will need to search for available journeys in order to book your trip. 
``` python

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
     
    print fares_result.requestStatus # True
```

### Create a Booking
Once you find the trip you want to book, you can proceed to make your booking
``` python
    # Create a passenger
    p1 = Passenger(
        id="PAX_SPEC_0",
        age=40,
        first_name="Jane",
        last_name="Smith")
    
    p1.add_contact(ContactInfo(CONTACT_TYPE.UNKNOWN, CONTACT_MEDIUM.PHONE, "123456789"))
    p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.PHONE, "123456789"))
    p1.add_contact(ContactInfo(CONTACT_TYPE.BUSINESS, CONTACT_MEDIUM.EMAIL, "jsmith@email.com"))
    
    # Specify travel segments
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
    
    # Add them to their respective legs
    leg1 = Leg(
        id="LS_1_1",
        travel_segments=[ts1])
    
    # Add the respective travel codes
    fc1 = FareCode(
        code="IXC-FOS-00700-STD-1",
        service_class="FIRST",
        travel_segment_id = "LS_1_1_TS_0",
        cabin_class="First",
        fare_display_name="Anytime Single (1st Class)")
    
    # Creating passenger reference
    pr1 = PassengerReference(p1, PASSENGER_TYPE.A, [fc1])
    
    # Specify the fare price breakdown for the total ticketable fare cost 
    price1 = FarePrice(319.52, "TICKET", "USD")
    
    # Specify all ticketable fares
    tf1 = TicketableFare(
            price= 319.52,
            prices = [price1],
            currency="GBP",
            passenger_references=[pr1])
    
    # Add the fare total
    f1 = FareTotal(
            id = "PRICE_P_1_23", 
            currency = "GBP", 
            price = 319.52, 
            expiration = "2015-10-27T15:50:33Z",
            ticketable_fares = [tf1],
            legs = [leg1])
    
    # Run booking request
    booking_result = sc.create_booking([f1], [p1])
    
    print booking_result.requestStatus.success # True
```

### Add payment
Once you have created a booking you can add payments to process the transaction.
``` python
    # Specify Billing Address
    b = BillingAddress(
            address1="9 Broad Court, Long Acre",
            city="London",
            zip_code="WC2B 5QN",
            country="GB",
            type=ADDRESS_TYPE.BUSINESS)
    
    # Specify Payment Method
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
```

### Update existing bookings
You can update your booking, add/remove ticket options, amend, etc.
``` python
    # Create ticket delivery option
    to1 = TicketOption(
        TICKET_DELIVERY_OPTION.VENDING_MACHINE,
        "GBP",
        0.00)
    
    # Add it to a BookingUpdate object
    bu = BookingUpdate(
                    record_locator=record_locator,
                    ticket_option=to1)
    
    booking_update = sc.update_booking(bu)
    
    print booking_update.requestStatus.success # True
``` 

### Confirm payment
Once you are happy with your booking, you can confirm your option.
``` python
# Create booking confirmation object
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


```
