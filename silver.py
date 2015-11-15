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

    def __init__(self, age=None, id=None, contact_info=[]):
        """Initializes passenger with attributes given

        Args:
           age (int):  The age of the passenger as integer.
           id (str):  The id of passenger - if not given, it's automatically generated.
        """

        if not id:
            self.id = Passenger._get_new_passenger_id()
        else:
            self.id = id
        
        self.age = age
        self.contact_info = contact_info


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

    def __init__(self, travel_points=[], 
                        fare_filter=FARE_FILTER.CHEAPEST,
                        passengers=[],
                        specs=[]):
        """ Initializes a fare search to find the relevant travel points for the passengers given.

        Args:
           travel_points (TravelPoint[]):  List of travel points.
           fare_filter (FARE_FILTER):  Fare filter type.
           passengers (Passenger[]):  List of passengers travelling.
           specs (TRAVEL_SPECS[]):  List of travel specifications.
        """

        self.travel_points = travel_points
        self.fare_filter = fare_filter
        self.passengers = passengers
        self.specs = specs


class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
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
        print xml

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













