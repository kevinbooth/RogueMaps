
"""
main.py
Main program that executes all the functions for RogueMaps
Created by Kevin Booth
Nov 15, 2017
"""

from api import GoogleMapsHelper
from document import DocumentCreator
from user import UserInterface


if __name__ == '__main__':
    UserInterface.welcome_message()
    user_data = UserInterface.retrieve_user_data()
    api_call_data = GoogleMapsHelper.api_call(user_data)
    massaged_data = GoogleMapsHelper.massage_api_response(api_call_data)
    created_pdf = DocumentCreator.create_pdf(massaged_data)
