"""
api.py
Module that provides Google Maps API functions
Created by Kevin Booth
Nov 15, 2017
"""

from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime
import googlemaps
import json



class GoogleMapsHelper:
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
        #directions_result = gmaps.directions(travel_information['start_address'],
        #                             travel_information['end_address'],
        #                             mode=travel_information['travel_mode'],
        #                             departure_time=now)

        directions_result = gmaps.directions('1 S Main St, Manchester NH 03102',
                                     '175 Canal St, Manchester NH 03101',
                                     mode='driving',
                                     departure_time=now)
        directions_result = json.dumps(directions_result)
        return json.loads(directions_result)[0]

    def massage_api_response(api_data):
        """
        Massages and manipulates the data retrieved from Google Maps to
        prepare it for PDF writing
        Returns: dictionary of strings and lists
        """
        return_dict = defaultdict(list)
        for instruction in api_data['legs'][0]['steps']:
            return_dict['instructions']
            .append(BeautifulSoup(instruction['html_instructions']).get_text())
        print(api_data['legs'][0]['steps'][0]['html_instructions'])
        print(' ')
        print(return_dict['instructions'])
