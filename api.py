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
    Provides functions to use the Google Maps API and format the response
    data
    """

    def api_call(travel_info):
        """
        Makes an API call to Google Maps and returns directions
        travel_info: dictionary with four keys:
            start_address
            end_address
            travel_mode
            depart_now
        Returns: JSON object
            or False on failure
        """
        gmap = googlemaps.Client(key='AIzaSyCtjrtull-lGC4jo0IwlSJBTAf8GhZkuSY')

        now = datetime.now()
        try:
            directions_result = gmap.directions(
                                                travel_info['start_address'],
                                                travel_info['end_address'],
                                                mode=travel_info['travel_mode'],
                                                departure_time=now
                                                )
        except:
            print('An Error occurred while retrieving directions')

        if 'directions_result' in locals():
            directions_result = json.dumps(directions_result)
            return json.loads(directions_result)[0]
        else:
            return False

    def massage_api_response(api_data):
        """
        Massages and manipulates the data retrieved from Google Maps to
        prepare it for PDF writing
        api_data: JSON object received from api_call function
        Returns: dictionary of strings and lists with the following keys:
            start_address
            end_address
            distance
            duration
            duration_in_traffic
            travel_mode
            instructions
            step_distance
        """
        return_dict = defaultdict(list)
        legs = api_data['legs'][0]

        return_dict['start_address'].append(legs['start_address'])
        return_dict['end_address'].append(legs['end_address'])
        return_dict['distance'].append(legs['distance']['text'])
        return_dict['duration'].append(legs['duration']['text'])
        if 'duration_in_traffic' in legs:
            (return_dict['duration_in_traffic']
             .append(legs['duration_in_traffic']['text']))
        return_dict['travel_mode'].append(legs['steps'][0]['travel_mode'])

        for instruction in legs['steps']:
            (return_dict['instructions']
             .append(BeautifulSoup(instruction['html_instructions'],
                                   'html.parser').get_text()))
            return_dict['step_distance'].append(instruction['distance'])
        return return_dict
