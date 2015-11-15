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
    C = "C"

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
                passenger_type=None,
                contact_info=[]):
        """Initializes passenger with attributes given

        Args:
           age (int):  The age of the passenger as integer.
           id (str):  The id of passenger - if not given, it's automatically generated.
           first_name (str):  First name of passenger.
           last_name (str):  Last name of passenger.
           passenger_type (PASSENGER_TYPE):  The class type of passenger travelling.
           contact_info (ContactInfo[]):  The contact information of the passenger.
        """

        if not id:
            self.id = Passenger._get_new_passenger_id()
        else:
            self.id = id
        
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.passenger_type = passenger_type
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

    def __init__(self, id, tarvel_segments):
        """FUNC_DESC.

        Args:
            id (str): The id of the leg
            trave_segments (TravelSegment[]): An array of travel segments.

        """

        self.id = id
        self.tarvel_segments = tarvel_segments

class TravelSegment:
    """
    This class represents a travel segment for a specific leg
    """

    def __init__(self, 
                    id = None,
                    sequence = None,
                    origin = None,
                    destination = None,
                    departure = None,
                    arrival = None,
                    designator = None,
                    marketing_carrier = None,
                    operating_carrier = None,
                    equipment_type = None,
                    equipment_type_str = None):
        """

        Args:
            id (str): The identifier of the travel segment.
            sequence (int): The ordering sequence number of the travel segment
            origin (str): The origin of the travel segment.
            destination (str): The destination of the travel segment.
            departure (DateTime): The datetime of departure of the travel segment.
            arrival (DateTime): The datetime of arrival of the travel segment.
            designator (str): The designator for the travel segment.
            marketing_carrier (str): The marketign carrier for the travel segment.
            operating_carrier (str): The operational carrier for the travel segment.
            equipment_type (str): The type of equipment for the travel segment defined by the silvercore equipment types.
            equipment_type_str (str): The printable string version of the equipment type.

        """

        self.id = id
        self.sequence = sequence
        self.origin = origin
        self.destination = destination
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

class TicketableFare:
    """ 
    Represents an individual section of a fare total, containing a set of fare codes and passengers
    """

    def __init__(self, 
                    price = None,
                    currency = None,
                    fare_codes = [],
                    passengers = []):
        """
        Args:
            price (int): The total amount of the ticketable fare.
            currency (str): The currency of the fare.
            fare_codes (FareCode[]): An array of fare codes for this ticketable fare.
            passengers (Passenger[]): An array of passengers for this ticketable fare.

        """

        self.price = price
        self.currency = currency
        self.fare_codes = fare_codes
        self.passengers = passengers

class FaresTotal:
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
        self.total_amount = total_amount
        self.leg_id = leg_id
        self.expiration = expiration
        self.segments = segments


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

        self.client = Client(SilverSoap.shopping_wsdl,
                            transport=HTTPSClientCertTransport(key, cert),
                            location=SilverSoap.shopping_location,
                            retxml=True)

    def _silver_send(self, api_func, xml_func, pyxb_xml):
        """Sends a raw xml message to the SilverCore backend with the function given with the func_enum provided.

        Args:
            api_func (SILVERCORE_API_FUNC): SilverCore functions available through the SOAP API.
            xml_func (SILVERCORE_XML_FUNC): The relevant silvercore xml element to create for the response

        Returns:
            SilverRaw.Element. A SilverRaw element containing the response of the SilverCore SOAP request::

        """

        # Adding SOAP Envelope wrapper
        senv = silvercore.Envelope()
        senv.Header = pyxb.BIND()
        senv.Body = pyxb.BIND()
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
        result = getattr(self.client.service, api_func)(__inject={"msg": xml})

        # Create respective SOAP SilverRaw object
        silver_obj = silvercore.CreateFromDocument(result)

        # Only one response object is supported at the time
        assert(len(silver_obj.Body.content()) == 1)

        # Return SilverCore response
        return silver_obj.Body.content()[0]


    def _get_xml_context(self):
        """Returns a pyxb BIND representation of a silverraw context object. In order for the context to be valid, it has to be assigned to an object's context property.

        Returns:
            pyxb.BIND. A pyxb.BIND object representing a silverraw context object::

        """

        return pyxb.BIND(
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

        p2p.pointToPointShoppingQuery = pyxb.BIND()

        # Setting Fare filter to the compatible SilverCore string
        p2p.pointToPointShoppingQuery.fareFilter = fare_query.fare_filter.value
        
        # Adding Travel Point Pairs
        p2p.pointToPointShoppingQuery.travelPointPairs = pyxb.BIND()

        i = 0
        for tp in fare_query.travel_points:
            p2p.pointToPointShoppingQuery.travelPointPairs.append(pyxb.BIND())
            p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].originTravelPoint = pyxb.BIND(tp.origin, type=tp.type)
            p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].destinationTravelPoint = pyxb.BIND(tp.destination, type=tp.type)

            if tp.departure:
                p2p.pointToPointShoppingQuery.travelPointPairs.travelPointPair[i].departureDateTimeWindow = \
                    pyxb.BIND(date=datetime.strftime(tp.departure, "%Y-%m-%d"), time=datetime.strftime(tp.departure, "%H:%M:%S"))

            i = i + 1

        for p in fare_query.passengers:
            p2p.pointToPointShoppingQuery.passengerSpecs = pyxb.BIND()
            p2p.pointToPointShoppingQuery.passengerSpecs.append(pyxb.BIND(passengerSpecID=p.id, age=p.age))

        # Send point to point search request
        response = self._silver_send(
            "PointToPointShop", 
            "pointToPointShoppingRequest", 
            p2p)

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


    def create_booking(self, fares, passengers):
        """Creates a booking with the fares and passengers given, and returns a response object

        Args:
            fares (FareTotal[]): An array of fares chosen to book.
            passengers (Passenger[]): An array of passengers that will be present on each booking.

        Returns:
            TYPE. DESC::

        """











