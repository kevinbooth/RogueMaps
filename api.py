"""
api.py
Module that provides Google Maps API functions
Created by Kevin Booth
Nov 15, 2018
"""

import googlemaps
from datetime import datetime
import json



class GoogleMaps:
    """
    Provides functions to use the Google Maps API
    """

    def api_call(travel_information):
        """
        Makes an API call to Google Maps and returns directions
        travel_information: dictionary with four keys - start_address,
        end_address, travel_mode, and depart_now
        Returns: JSON object
        """
        gmaps = googlemaps.Client(key='AIzaSyCtjrtull-lGC4jo0IwlSJBTAf8GhZkuSY')

        now = datetime.now()
        directions_result = gmaps.directions(travel_information['start_address'],
                                     travel_information['end_address'],
                                     mode=travel_information['travel_mode'],
                                     departure_time=now)

        #direction_data = json.loads(str(directions_result))
        print(json.dumps(directions_result))
