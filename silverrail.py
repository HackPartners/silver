

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

        return "PAX_" + str(passenger_count++)

    __init__(self, age=None, id=None, contact_info=[]):
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

    def __init__(self, origin=None, destination=None, departure=None, arrival=None):
        """Initializes the Travelpoint with the relevant origin and destination, and optional departure and arrival times.

        Args:
           origin (str):  Name of station of origin.
           destination (str):  Name of station of arrival.
           departure (DateTime):  Approximate time and date of departure.
           arrival (DateTime):  Approximate time and date of arrival.
        """
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival


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


class SilverCore:
    """
    The SilerCore class manages all interactions with the SilverCore API.

    This exposes a simple interface for p2p search, bookings, and payemnts.

    .. note::

       For more thorough documentation check the SilverRail wikipedia.

    """

    def __init__(self, distributor, point_of_sale, channel):
        """Gathers the information required to create the context on each request.

        Args:
           distributor (str):  The name of the distributor for the SilverRail ticketing system provider.
           point_of_sale (str):  The point of sale, which can be location, etc. 
           channel (str):  The channel code for the queries. 
        """

        self._distributor = distributor
        self._point_of_sale = point_of_sale
        self._channel = channel

    def verify(self, cert_locat, pwd):
        """Retreives the location of the certificate to use as ssl verification with each of the requests..

        Args:
           cert_locat (str):  The absolute location for the ssl silverrail certificate that will be used to verify each request.
           pwd (str):  The password used alongside with the certificate. 


        .. note::

           Remember never to hardcode the password in the python files. Always set it in the bash environment and request it with pwd = os.ENV["SILVERCORE_PASSWORD"].
        """

        self._cert_locat = cert_locat
        self._pwd = pwd

    def search_fare(self, fare_query):
        """FUNC_DESC.

        Args:
            fare_query (FareSearch): The fare search object to query the silvercore backend with

        Returns:
            FareResult. The results from the FareQuery::

        """

        return { success: True }













