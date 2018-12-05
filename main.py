
"""
main.py
Main program that executes all the functions for RogueMaps
Created by Kevin Booth
Nov 15, 2018
"""

from api import GoogleMapsHelper
from document import DocumentCreator
from user import UserInterface


if __name__ == '__main__':
    UserInterface.welcome_message()
    user_data = UserInterface.retrieve_user_data()
    api_call_data = GoogleMapsHelper.api_call(user_data)

    if api_call_data is False:
        print('Please try again')
    else:
        massaged_data = GoogleMapsHelper.massage_api_response(api_call_data)
        full_file_path = DocumentCreator.create_pdf(massaged_data)
        if user_data['depart_now'] == 'y':
            DocumentCreator.open_document(full_file_path)
        elif user_data['depart_now'] == 'n':
            print("Directions pdf created in: " + full_file_path)
