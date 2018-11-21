"""
main.py
Main program that executes all the functions for RogueMaps
Created by Kevin Booth
Nov 15, 2017
"""

from api import GoogleMapsHelper
from user import UserInterface
import googlemaps
from datetime import datetime



if __name__ == '__main__':
    UserInterface.welcome_message()
    user_data = UserInterface.user_data_retrieval()
    api_call = GoogleMapsHelper.api_call(user_data)
    api_data = GoogleMapsHelper.massage_api_response(api_call)
