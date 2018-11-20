"""
main.py
Main program that executes all the functions for RogueMaps
Created by Kevin Booth
Nov 15, 2017
"""

from api import GoogleMaps
from user import UserInterface
import googlemaps
from datetime import datetime



if __name__ == '__main__':
    UserInterface.welcome_message()
    user_data = UserInterface.user_data_retrieval()
    GoogleMaps.api_call(user_data)
