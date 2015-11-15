from silverraw import silvershop, silvercom, silverbook, silvercore

import os

from datetime import datetime
from enum import Enum
import pyxb

# Imports for suds
import urllib2, httplib, socket
from suds.client import Client
from suds.sax.text import Raw
from suds.transport.http import HttpTransport, Reply, TransportError


# Making binding easier to use
b=pyxb.BIND


class TRAVEL_TYPE:
    STATION = "STATION"

class FARE_FILTER(Enum):
    NONE = "NONE"
    CHEAPEST = "CHEAPEST"
    CHEAPEST_ONEWAY_AND_ROUNDTRIP = "CHEAPEST_ONEWAY_AND_ROUNDTRIP"
    OPEN = "OPEN"
    CHEAPEST_OPEN = "CHEAPEST_OPEN"

class CONTACT_TYPE(Enum):
    HOME = "HOME"
    BUSINESS = "BUSINESS"
    UNKNOWN = "UNKNOWN"

class CONTACT_MEDIUM(Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"

class PASSENGER_TYPE(Enum):
    A = "A"
    C = "C"

class ADDRESS_TYPE(Enum):
    BUSINESS = "BUSINESS"

class PAYMENT_TYPE(Enum):
    CREDIT_CARD = "CC"
    ON_ACCOUNT = "OA"
    DEBIT_CARD = "DB"

class CONFIRMATION_TYPE(Enum):
    CREDIT_CARD = "CC"
    DEBIT_CARD = "DB"
    ID_CARD = "ID"
    LOYALTY_CARD = "LC"

class TICKET_DELIVERY_OPTION(Enum):
    EMAIL = "EML"
    E_TICKET = "ETK"
    PRINT_AT_HOME = "PAH"
    SMS = "SMS"
    CONDUCTOR = "TBC"
    REGULAR_MAIL = "TBM"
    OVERNIGHT_MAIL = "TBO"
    EXPRESS_MAIL = "TBX"
    METRO_LINK = "TML"
    TICKETING_OFFICE = "TOF"
    VENDING_MACHINE = "TVM"

class TicketOption:
    """
    Represents a ticket option to add, modify or remove an existing booking
    """

    def __init__(self, code, currency, fee):
        """
        Args:
            code (TICKET_DELIVERY_OPTION): Type of ticket option.
            currency (str): Currency of fees involved.
            fee (int): Amount infolved as fee in order to have this ticket option.

        """
        self.code = code
        self.currency = currency
        self.fee = fee

class BookingUpdate:
    """
    This class represents a booking update, and allows users to add/remove fees, ticket delivery option/fee, adding passenger IDs, leg solutions, etc.
    """

    def __init__(self, 
                    record_locator = None,
                    ticket_option = None):
        """
        Args:
            record_locator (str): The identifier of the booking record.
            ticket_option (TicketOption): A TicketOption object specifying the option to add to a specific booking
        """

        self.record_locator = record_locator
        self.ticket_option = ticket_option

class BookingConfirmation:
    """ 
    This class represents a booking confirmation.
    """

    def __init__(self, 
                    record_locator = None,
                    confirmation_type = None,
                    card_number = None,
                    expiration_year=2016,
                    expiration_month=12,
                    card_holder_first_name = None,
                    card_holder_last_name = None):
        """
        Args:
            record_locator (str): The identifier of the booking record.
            confirmation_type (CONFIRMATION_TYPE): The form of confirmation for the booking.
            card_number (str): The card number.
            expiration_year (int): The year of expiration of card.
            expiration_month (int): The month of expiration of card.
            card_holder_first_name (str): The first name of card holder.
            card_holder_last_name (str): The last name of card holder.

        """

        self.record_locator = record_locator
        self.confirmation_type = confirmation_type
        self.card_number = card_number
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.card_holder_first_name = card_holder_first_name
        self.card_holder_last_name = card_holder_last_name

class BillingAddress:
    """
    This class represents a billing address. It is mostly used for payemnts.
    """

    def __init__(self, 
                    address1 = None,
                    city = None,
                    zip_code = None,
                    country = None,
                    type = None):
        """
        Args:
            address1 (str): Your first line of billing address.
            city (str): Your billing city.
            zip_code (str): Your billing zip code.
            country (str): The country of your billing address.
            type (ADDRESS_TYPE): The type of payemnt.
        """

        self.address1 = address1
        self.city = city
        self.zip_code = zip_code
        self.country = country
        self.type = type

class PaymentMethod:
    """
    This class represents a payment method for use in SilverCore API.
    """

    def __init__(self, 
                    record_locator = None,
                    payment_form = None,
                    payment_form_type = None,
                    card_number = None,
                    card_type = None,
                    card_holder_first_name = None,
                    card_holder_last_name = None,
                    card_validation_number = None,
                    amount = None,
                    currency = None,
                    expiration_year = None,
                    expiration_month = None,
                    customer_ip_address = None,
                    billing_address = None,
                    response_spec = None):

        self.record_locator = record_locator
        self.payment_form = payment_form
        self.payment_form_type = payment_form_type
        self.card_number = card_number
        self.card_type = card_type
        self.card_holder_first_name = card_holder_first_name
        self.card_holder_last_name = card_holder_last_name
        self.card_validation_number = card_validation_number
        self.amount = amount
        self.currency = currency
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.customer_ip_address = customer_ip_address
        self.billing_address = billing_address
        self.response_spec = response_spec

class ContactInfo:
    """
    Represents contact information for a passenger
    """

    def __init__(self, type, medium, info):
        self.type = type
        self.medium = medium
        self.info = info

class Passenger:
    """Represents a passenger that will be on the relevant trip.

    The passenger generates a unique ID whenever it is created.
    """
    
    passenger_count = 0

    @staticmethod
    def _get_new_passenger_id():
        """This function returns a unique id to create a passenger.

        Returns:
           str.  The unique id for the passenger::

           """

        Passenger.passenger_count = Passenger.passenger_count+1
        return "PAX_" + str(Passenger.passenger_count)

    def __init__(self, 
                age=None, 
                id=None,
                first_name=None,
                last_name=None,
                contact_info=[]):
        """Initializes passenger with attributes given

        Args:
           age (int):  The age of the passenger as integer.
           id (str):  The id of passenger - if not given, it's automatically generated.
           first_name (str):  First name of passenger.
           last_name (str):  Last name of passenger.
           contact_info (ContactInfo[]):  The contact information of the passenger.
        """

        if not id:
            self.id = Passenger._get_new_passenger_id()
        else:
            self.id = id
        
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.contact_info = contact_info

    def add_contact(self, contact_info):
        assert(isinstance(contact_info, ContactInfo))
        self.contact_info.append(contact_info)

class TravelPoint:
    """
    Stores a pair of origin and destination location as well as the time of departure and arrival
    """

    def __init__(self, origin=None, destination=None, departure=None, arrival=None, type=TRAVEL_TYPE.STATION):
        """Initializes the Travelpoint with the relevant origin and destination, and optional departure and arrival times.

        Args:
           origin (str):  Name of station of origin.
           destination (str):  Name of station of arrival.
           departure (DateTime):  Approximate time and date of departure.
           arrival (DateTime):  Approximate time and date of arrival.
        """

        if not departure and not arrival:
            raise Exception("You must supply either departure time, arrival time.")

        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.type = type


class FareSearch:
    """
    Represents an object which contains all required fields to perform a successful fare search
    """

    def __init__(self, travel_points=[], 
                        fare_filter=FARE_FILTER.CHEAPEST,
                        passengers=[],
                        specs=[]):
        """ Initializes a fare search to find the relevant travel points for the passengers given.

        Args:
           travel_points (TravelPoint[]):  List of travel points.
           fare_filter (FARE_FILTER):  Fare filter type.
           passengers (Passenger[]):  List of passengers travelling.
           specs (TRAVEL_SPECS[]):  [Not supported yet] List of travel specifications.
        """

        self.travel_points = travel_points
        self.fare_filter = fare_filter
        self.passengers = passengers

        # TODO: Specs are not supported yet
        self.specs = specs

class Leg:
    """
    Represents a travel leg with its respective travel segments
    """

    def __init__(self, id, travel_segments):
        """FUNC_DESC.

        Args:
            id (str): The id of the leg
            trave_segments (TravelSegment[]): An array of travel segments.

        """

        self.id = id
        self.travel_segments = travel_segments

class TravelSegment:
    """
    This class represents a travel segment for a specific leg
    """

    def __init__(self, 
                    type="TRAIN",
                    id = None,
                    sequence = None,
                    origin = None,
                    origin_type = "STATION",
                    destination = None,
                    destination_type = "STATION",
                    departure = None,
                    arrival = None,
                    designator = None,
                    marketing_carrier = None,
                    operating_carrier = None,
                    equipment_type = None,
                    equipment_type_str = None):
        """

        Args:
            type (str): The type for the medium for transport
            id (str): The identifier of the travel segment.
            sequence (int): The ordering sequence number of the travel segment
            origin (str): The origin of the travel segment.
            origin_type (str): The type of origin of the travel segment.
            destination (str): The destination of the travel segment.
            destination_type (str): The destination type of the travel segment.
            departure (DateTime): The datetime of departure of the travel segment.
            arrival (DateTime): The datetime of arrival of the travel segment.
            designator (str): The designator for the travel segment.
            marketing_carrier (str): The marketign carrier for the travel segment.
            operating_carrier (str): The operational carrier for the travel segment.
            equipment_type (str): The type of equipment for the travel segment defined by the silvercore equipment types.
            equipment_type_str (str): The printable string version of the equipment type.

        """

        self.id = id
        self.type = type
        self.sequence = sequence
        self.origin = origin
        self.origin_type = origin_type
        self.destination = destination
        self.destination_type = destination_type
        self.departure = departure
        self.arrival = arrival
        self.designator = designator
        self.marketing_carrier = marketing_carrier
        self.operating_carrier = operating_carrier
        self.equipment_type = equipment_type
        self.equipment_type_str = equipment_type_str

class FareCode:
    """
    Represents a fare code for the respective Ticketable Fare
    """

    def __init__(self, 
                    code = None,
                    service_class = None,
                    travel_segment_id = None,
                    cabin_class = None,
                    fare_display_name = None):
        """
        Args:
            code (str): The code that identifies the fare code
            service_class (str): The type of service class
            travel_segment_id (str): The travel segment it references
            cabin_class (str): The class of the cabin for the travel segment
            fare_display_name (str): The display name for the fare code

        """

        self.code = code
        self.service_class = service_class
        self.travel_segment_id = travel_segment_id
        self.cabin_class = cabin_class
        self.fare_display_name = fare_display_name


class FarePrice:
    """
    Class representing the breakdown costs of a fare total
    """

    def __init__(self, price, type, currency):
        """

        Args:
            price (int): The price of the current fare breakdown item
            type (str): The type of the fare price breakdown item
            currency (str): The currency of the fare price breakdown item

        """

        self.price = price
        self.type = type
        self.currency = currency

class PassengerReference:
    """
    An agregation of a passenger with respective fare codes for a ticketable fare
    """

    def __init__(self, passenger, class_type, fare_codes):
        """
        Args:
            ARG (TYPE): DESC1
            passenger (Passenger[]): The passenger for this reference.
            class_type (PASSENGER_TYPE):  The class type of passenger travelling.
            fare_codes (FareCode[]): An array of fare codes for this passenger.

        """

        self.passenger = passenger
        self.class_type = class_type
        self.fare_codes = fare_codes


class TicketableFare:
    """ 
    Represents an individual section of a fare total, containing a set of fare codes and passengers
    """

    def __init__(self, 
                    price = None,
                    prices = [],
                    currency = None,
                    passenger_references = []):
        """
        Args:
            price (int): The total amount of the ticketable fare.
            prices (FarePrice[]): Array of prices for the breakdown of the total
            currency (str): The currency of the fare.
            passenger_references (PassengeReference[]): An array of passenger references for this ticketable fare.

        """

        self.price = price
        self.prices = prices
        self.currency = currency
        self.passenger_references = passenger_references

class FareTotal:
    """
    This class represents a fare for a specific leg, with specific segments given
    """

    def __init__(self, 
                    id = None,
                    currency = None,
                    price = None,
                    expiration = None,
                    ticketable_fares = [],
                    legs = []):
        """

        Args:
            id (str): The identifier for this fare
            currency (str): the currency for the fare amount
            price (int): The of the total cost fare 
            expiration (DateTime): The date of expiration for the fare
            ticketable_fares (TicketableFare[]): Array of ticketable fares comprising this fare
            legs (Leg[]): Array of legs that this fare refers to, minimum 1.

        """

        self.id = id
        self.currency = currency
        self.price = price
        self.expiration = expiration
        self.ticketable_fares = ticketable_fares
        self.legs = legs


class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    """ 
    This class handles authentication in the secure ssl tunnel created with the given PEM certificate and RSA key
    """

    def __init__(self, key, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        #Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        return httplib.HTTPSConnection(host,
                                       key_file=self.key,
                                       cert_file=self.cert)

class HTTPSClientCertTransport(HttpTransport):
    """ 
    This class creates an SSL tunnel to establish the secure connection between the silverclient and silvercore API
    """

    def __init__(self, key, cert, *args, **kwargs):
        HttpTransport.__init__(self, *args, **kwargs)
        self.key = key
        self.cert = cert

    def u2open(self, u2request):
        """
        Open a connection.
        @param u2request: A urllib2 request.
        @type u2request: urllib2.Requet.
        @return: The opened file-like urllib2 object.
        @rtype: fp
        """
        tm = self.options.timeout
        url = urllib2.build_opener(HTTPSClientAuthHandler(self.key, self.cert))
        if self.u2ver() < 2.6:
            socket.setdefaulttimeout(tm)
            return url.open(u2request)
        else:
            return url.open(u2request, timeout=tm)


class SilverSoap:
    """
    The SilverSoap class manages all interactions with the SilverCore API.

    This class deals with the heavy conversion of objects to their respective SilverRaw format.

    .. note::

       For more thorough documentation check the SilverRail wikipedia.

    """

    booking_wsdl="https://hacktrain.railgds.net/booking-ws/services/Booking/v2?wsdl"
    booking_location="https://hacktrain.railgds.net/booking-ws/services/Booking/v2"
    shopping_wsdl="https://hacktrain.railgds.net/shopping-ws/services/Shopping/v2?wsdl"
    shopping_location="https://hacktrain.railgds.net/shopping-ws/services/Shopping/v2"

    def __init__(self, distributor, point_of_sale, channel, cert, key):
        """Gathers the information required to create the context on each request.

        Args:
           distributor (str):  The name of the distributor for the SilverRail ticketing system provider.
           point_of_sale (str):  The point of sale, which can be location, etc. 
           channel (str):  The channel code for the queries.
           cert (str):  The absolute path location for the ssl silverrail certificate that will be used to verify each request.
           key (str):  The absolute path location of the key file.

        """

        self._distributor = distributor
        self._point_of_sale = point_of_sale
        self._channel = channel

        self.shop_client = Client(SilverSoap.shopping_wsdl,
                            transport=HTTPSClientCertTransport(key, cert),
                            location=SilverSoap.shopping_location,
                            retxml=True)

        self.book_client = Client(SilverSoap.booking_wsdl,
                            transport=HTTPSClientCertTransport(key, cert),
                            location=SilverSoap.booking_location,
                            retxml=True)

    def _silver_send(self, soap_client, api_func, xml_func, pyxb_xml):
        """Sends a raw xml message to the SilverCore backend with the function given with the func_enum provided.

        Args:
            soap_client (SILVERCORE_API_CLIENT): The SOAP client to use for the request.
            api_func (SILVERCORE_API_FUNC): SilverCore functions available through the SOAP API.
            xml_func (SILVERCORE_XML_FUNC): The relevant silvercore xml element to create for the response

        Returns:
            SilverRaw.Element. A SilverRaw element containing the response of the SilverCore SOAP request::

        """
        # Adding SOAP Envelope wrapper
        senv = silvercore.Envelope()
        senv.Header = b()
        senv.Body = b()
        getattr(senv.Body, xml_func).append(pyxb_xml)

        xml = str(senv.toxml())

        # Until nasty pyxb bug is fixed, we need to add namespace manually.
        # Basically, when we append a pyxb object to a _PluralObject, 
        # the namespace for that object is not updated, so we have to add
        # it manually.
        # If anyone can submit a pull request to pyxb to fix it, or 
        # find a neater walkaround, let's do it.
        xml = xml.replace(xml_func + ">", "ns3:" + xml_func + ">")

        # Call the relevant SilverCore function with the raw XML given 
        client_found = getattr(self, soap_client)
        result = getattr(client_found.service, api_func)(__inject={"msg": xml})

        # Create respective SOAP SilverRaw object
        silver_obj = silvercore.CreateFromDocument(result)

        # Only one response object is supported at the time
        assert(len(silver_obj.Body.content()) == 1)

        # Return SilverCore response
        return silver_obj.Body.content()[0]


    def _get_xml_context(self):
        """Returns a pyxb BIND representation of a silverraw context object. In order for the context to be valid, it has to be assigned to an object's context property.

        Returns:
            b. A b object representing a silverraw context object::

        """

        return b(
            distributorCode="HACKTRAIN", 
            pointOfSaleCode="GB", 
            channelCode="CH1")

    def _search_fare(self, fare_query):
        """This function creates the respective SOAP object from the FareQuery object and returns the results found from the API.

        Args:
            fare_query (FareSearch): The fare search object to query the silvercore backend with

        Returns:
            FareResult. The results from the FareQuery::

        """

        # Creating a point to point shopping request
        p2p = silvershop.pointToPointShoppingRequest()

        # Obtaining the context
        p2p.context = self._get_xml_context()

        p2p.pointToPointShoppingQuery = b()

        # Setting Fare fixlter to the compatible SilverCore string
        p2p.pointToPointShoppingQuery.fareFilter = fare_query.fare_filter.value
        
        # Adding Travel Point Pairs
        p2p.pointToPointShoppingQuery.travelPointPairs = b()

        i = 0
        for tp in fare_query.travel_points:
            p2p.pointToPointShoppingQuery.travelPointPairs.append(b())
            p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].originTravelPoint = b(tp.origin, type=tp.type)
            p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].destinationTravelPoint = b(tp.destination, type=tp.type)

            if tp.departure:
                p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].departureDateTimeWindow = \
                    b(date=datetime.strftime(tp.departure, "%Y-%m-%d"), time=datetime.strftime(tp.departure, "%H:%M:%S"))

            i = i + 1

        for p in fare_query.passengers:
            p2p.pointToPointShoppingQuery.passengerSpecs = b()
            p2p.pointToPointShoppingQuery.passengerSpecs.append(b(passengerSpecID=p.id, age=p.age))

        # Send point to point search request
        response = self._silver_send(
            "shop_client",
            "PointToPointShop", 
            "pointToPointShoppingRequest", 
            p2p)

        return response

    def _create_booking(self, fares, passengers, parameters, response_specs):
        """Creates the relevant silverraw objects and sends a create booking request to the silvercore api.

        Args:
            fares (FareTotal[]): An array of fares chosen to book.
            passengers (Passenger[]): An array of passengers that will be present on each booking.
            parameters (CREATE_BOOKING_PARAMS[]): Array of parameters to pass the create booking request (NOT SUPPORTED YET).
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API.

        Returns:
            silverraw.createBookingResponse. Returns a createBookingResponse object::

        """

        cb = silverbook.createBookingRecordRequest()
        
        # Obtaining the context
        cb.context = self._get_xml_context()

        # TODO: Add support for parameters        
        cb.parameters = b()
        cb.parameters.priceAcceptance = b()
        cb.parameters.priceAcceptance.acceptAny = True

        # if len(response_specs):
        #     cb.responseSpec = b()
        #     for r in response_specs:
        #         getattr(cb.responseSpec, r) = True

        # Adding passengers
        cb.passengers = b()
        for idx1, passenger in enumerate(passengers):

            cb.passengers.passenger.append(b())

            p = cb.passengers.passenger[idx1]

            p.passengerID           = passenger.id
            p.nameFirst             = passenger.first_name
            p.nameLast              = passenger.last_name
            p.ageAtTimeOfTravel     = 40

            p.contactInformation = b()

            # Adding all contact information available for passenger
            for contact in passenger.contact_info:
                p.contactInformation.contact.append(b(
                        contactType=contact.type.value,
                        contactMedium=contact.medium.value, 
                        contactInfo=contact.info))

        # Adding point to point prices
        cb.prices = b()
        for idx2, fare in enumerate(fares):

            cb.prices.pointToPointPrice.append(b())

            pr = cb.prices.pointToPointPrice[idx2]
            pr.priceID = fare.id
            pr.totalPrice = b(fare.price, currency=fare.currency)
            pr.holdExpiration = fare.expiration

            pr.legReferences = b()

            for leg in fare.legs:
                pr.legReferences.legSolutionIDRef.append(b(leg.id))

            # Add all ticketable fares
            pr.ticketableFares = b()
            for idx5, ticketable in enumerate(fare.ticketable_fares):

                pr.ticketableFares.ticketableFare.append(b())

                tf = pr.ticketableFares.ticketableFare[idx5]
                tf.totalPrice = b(ticketable.price, currency=ticketable.currency)

                # Adding all price breakdown
                tf.prices = b()
                for price in ticketable.prices:
                    tf.prices.price.append(b(price.price, type=price.type, currency=price.currency))

                # Adding passenger references
                tf.passengerReferences = b()
                for idx6, p_ref in enumerate(ticketable.passenger_references):

                    tf.passengerReferences.passengerReference.append(b())

                    r = tf.passengerReferences.passengerReference[idx6]
                    r.passengerIDRef = p_ref.passenger.id
                    r.passengerTypeCode = p_ref.class_type.value

                    # Adding fare codes
                    r.fareCodes = b()
                    for id7, farecode in enumerate(p_ref.fare_codes):
                        r.fareCodes.fareCode.append(b())

                        fc = r.fareCodes.fareCode[id7]
                        fc.code = farecode.code
                        fc.serviceClass = farecode.service_class
                        fc.travelSegmentIDRef = farecode.travel_segment_id
                        fc.cabinClass = farecode.cabin_class
                        fc.fareDisplayName = farecode.fare_display_name

            # Adding all legs for trip
            cb.legSolutions = b()
            for idx3, leg in enumerate(fare.legs):

                cb.legSolutions.legSolution.append(b())

                l = cb.legSolutions.legSolution[idx3]
                l.legSolutionID = leg.id

                # Adding all travel segments for each leg
                l.travelSegments = b()

                for idx4, segment in enumerate(leg.travel_segments):

                    l.travelSegments.travelSegment.append(b())

                    ts = l.travelSegments.travelSegment[idx4]

                    ts.sequence                 = segment.sequence
                    ts.travelSegmentID          = segment.id
                    ts.type                     = segment.type
                    ts.originTravelPoint        = b(segment.origin, type=segment.origin_type)
                    ts.destinationTravelPoint   = b(segment.destination, type=segment.destination_type)
                    ts.departureDateTime        = segment.departure
                    ts.arrivalDateTime          = segment.arrival
                    ts.designator               = segment.designator
                    ts.marketingCarrier         = segment.marketing_carrier
                    ts.operatingCarrier         = segment.operating_carrier
                    ts.equipmentType            = b(segment.equipment_type_str, code=segment.equipment_type)

        # Send create booking request
        response = self._silver_send(
            "book_client",
            "CreateBookingRecord", 
            "createBookingRecordRequest", 
            cb)

        return response

    def _add_payment(self, payment, response_specs):
        """Creates the SilverRaw SOAP objects to communicate to the AddPayment API and add the payment given by the silver.PaymentMethod object

        Args:
            payment (PaymentMethod): The payment method to use.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.addPaymentResponse. Returns a addPaymentResponse object::

        """

        ap = silverbook.addPaymentRequest()
        
        # Get context
        ap.context = self._get_xml_context()

        # Record locator to identify booking
        ap.recordLocator = payment.record_locator

        # Adding method of payment
        ap.payment = b()
        ap.payment.formOfPayment                    = b(payment.payment_form, type=payment.payment_form_type.value)
        ap.payment.creditCard                       = b(type = payment.card_type)
        ap.payment.creditCard.number                = payment.card_number
        
        expiration_ym = str(payment.expiration_year) + "-" + str(payment.expiration_month)
        ap.payment.creditCard.expirationYearMonth   = b(expiration_ym)
        
        fl_name = payment.card_holder_first_name + " " + payment.card_holder_last_name
        ap.payment.creditCard.cardholderName        = fl_name
        
        billing_address = payment.billing_address
        ba = b(address1=billing_address.address1, 
                city=billing_address.city, 
                zipCode=billing_address.zip_code, 
                country=billing_address.country, 
                addressType=billing_address.type.value)

        ap.payment.creditCard.billingAddress        = ba
        ap.payment.creditCard.validationNumber      = payment.card_validation_number
        ap.payment.amount                           = b(payment.amount, currency=payment.currency)

        print ap.payment.creditCard.billingAddress.toxml()
        print ap.payment.creditCard.toxml()

        response = self._silver_send(
            "book_client",
            "AddPaymentRequest", 
            "addPaymentRequest", 
            ap)

        return response

    def _update_booking(self, booking_update, response_specs):
        """
        Creates an silverraw update booking object based on the update options given and calls the silvercore api with the objects created.

        Args:
            booking_update (BookingUpdate): A booking update with the relevant booking update options.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.updateBookingRecordRequest. Returns an updateBookingRecordRequest object::

        """

        bu = silverbook.updateBookingRecordRequest()

        # Adding context
        bu.context = self._get_xml_context()

        # Adding booking record id
        bu.recordLocator = booking_update.record_locator

        # Adding ticket option information
        to = booking_update.ticket_option
        if to:
            bu.fulfillmentInformation = b()
            bu.fulfillmentInformation.ticketOption = b()
            bu.fulfillmentInformation.ticketOption.code = to.code.value
            bu.fulfillmentInformation.ticketOption.code.fee = b(to.fee, currency=to.currency)

        response = self._silver_send(
            "book_client",
            "UpdateBookingRecordRequest", 
            "updateBookingRecordRequest", 
            bu)

        return response

    def _confirm_booking(self, confirmation, response_specs=[]):
        """Creates the SilverRaw objects necessary to send a booking confirmation request to the server

        Args:
            confirmation (BookingConfirmation): The confirmation details to finalise and confirm booking.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.confirmBookingResponse. Returns a confirmBookingResponse object::

        """

        cb = silverbook.confirmBookingRecordRequest()

        # Retreiving context
        cb.context = self._get_xml_context()

        # Record locator
        cb.recordLocator = confirmation.record_locator
        cb.confirmationInformation = b()

        cb.confirmationInformation
        cb.confirmationInformation.selectedConfirmationOption = b()

        expiration_ym = str(confirmation.expiration_year) + "-" + str(confirmation.expiration_month)

        conf_opt = b(cardholderNameLast=confirmation.card_holder_last_name, 
                cardholderNameFirst=confirmation.card_holder_first_name, 
                cardNumber=confirmation.card_number, 
                expirationYearMonth=expiration_ym)

        cb.confirmationInformation.selectedConfirmationOption.creditCardOption = conf_opt

        response = self._silver_send(
            "book_client",
            "ConfirmBookingRecordRequest", 
            "confirmBookingRecordRequest", 
            cb)

        return response

class SilverCore(SilverSoap):
    """
    The SilerCore class manages all interactions with the client and hides all the complexity from the SilverCore SOAP interface.

    This exposes a simple interface for p2p search, bookings, and payemnts.

    .. note::

       For more thorough documentation check the SilverRail wikipedia.

    """

    def __init__(self, distributor, point_of_sale, channel, cert=None, key=None):
        """Gathers the information required to create the context on each request.

        Args:
           distributor (str):  The name of the distributor for the SilverRail ticketing system provider.
           point_of_sale (str):  The point of sale, which can be location, etc. 
           channel (str):  The channel code for the queries. 
           cert (str):  The absolute path location for the ssl silverrail certificate that will be used to verify each request.
           key (str):  The absolute path location of the key file.


        .. note::

           Remember never to hardcode the password in the python files. Always set it in the bash environment and request it with pwd = os.ENV["SILVERCORE_PASSWORD"].
        """

        cert = cert or os.environ.get("SILVERCORE_CERT")
        key = key or os.environ.get("SILVERCORE_KEY")

        if not cert or not key:
            raise Exception("Certificate and key absolute paths must be provided")

        # Initializes it's parent SilverSoap class which will deal with all the heavy SOAP lifting.
        SilverSoap.__init__(self, distributor, point_of_sale, channel, cert, key)


    def set_credentials(self, cert_locat, pwd):
        """Retreives the location of the certificate to use as ssl verification with each of the requests..

        Args:
           cert_locat (str):  The absolute location for the ssl silverrail certificate that will be used to verify each request.
           pwd (str):  The password used alongside with the certificate. 


        .. note::

           Remember never to hardcode the password in the python files. Always set it in the bash environment and request it with pwd = os.ENV["SILVERCORE_PASSWORD"].
        """

        self._set_credentials(cert_locat, pwd)

    def search_fare(self, fare_query):
        """This function handles handles the fare_query object and returns the legs found and their respective fare results found.

        Args:
            fare_query (FareSearch): The fare search object to query the silvercore backend with

        Returns:
            FareResult. The results from the FareQuery::

        """

        return self._search_fare(fare_query)


    def create_booking(self, fares, passengers, parameters=[], response_specs = []):
        """Creates a booking with the fares and passengers given, and returns a response object

        Args:
            fares (FareTotal[]): An array of fares chosen to book.
            passengers (Passenger[]): An array of passengers that will be present on each booking.
            parameters (CREATE_BOOKING_PARAMS[]): Array of parameters to pass the create booking request  (NOT SUPPORTED YET).
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.createBookingResponse. Returns a createBookingResponse object::

        """

        return self._create_booking(fares, passengers, parameters, response_specs)

    def add_payment(self, payment, response_specs=[]):
        """Adds a form of payment to an existing booking referenced throuhg a record locator object

        Args:
            payment (PaymentMethod): The payment method to use.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.addPaymentResponse. Returns a addPaymentResponse object::

        """

        return self._add_payment(payment, response_specs)

    def update_booking(self, booking_update, response_specs=[]):
        """
        Args:
            booking_update (BookingUpdate): A booking update with the relevant booking update options.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.updateBookingRecordRequest. Returns an updateBookingRecordRequest object::

        """
        return self._update_booking(booking_update, response_specs)

    def confirm_booking(self, confirmation, response_specs=[]):
        """Confirms the booking assuming that payments have been added and everything has been finalised

        Args:
            confirmation (BookingConfirmation): The confirmation details to finalise and confirm booking.
            response_specs (CREATE_BOOKING_SPECS[]): Array of specs for the response from the SilverCore API (NOT SUPPORTED YET).

        Returns:
            silverraw.confirmBookingResponse. Returns a confirmBookingResponse object::

        """

        return self._confirm_booking(confirmation, response_specs)





