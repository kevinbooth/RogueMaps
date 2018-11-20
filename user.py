"""
user.py
Module that provides user specific functions
Created by Kevin Booth
Nov 15, 2017
"""


class UserInterface:
    """
    Provides user interface functions
    """

    def welcome_message():
        """
        Provides welcome messages to the user
        """
        print('Welcome to RogueMaps where you can save your directions into a PDF')

    def user_data_retrieval():
        """
        Retrieves data about directions from the user
        Returns: dictionary
            starting destination
            ending destination
            mode of transportation
        """
        start_street = input('Please enter the starting street address (ex: 1 Main St): ')
        start_city = input('Please enter the starting city (ex: Manchester): ')
        start_state = input('Please enter the starting state (ex: NH): ')
        start_zipcode = input('Please enter the starting zipcode (ex: 03101): ')

        start_address = str(start_street) + ', ' + str(start_city) + ' ' + str(start_state) + ' ' + str(start_zipcode)

        end_street = input('Please enter the destination street address (ex: 1 Maple St): ')
        end_city = input('Please enter the destination city (ex: Nashua): ')
        end_state = input('Please enter the destination state (ex: NH): ')
        end_zipcode = input('Please enter the destination zipcode (ex: 03061): ')

        end_address = str(end_street) + ', ' + str(end_city) + ' ' + str(end_state) + ' ' + str(end_zipcode)

        travel_mode = input('Please choose from the following travel modes: walking, bicycling, transit, or driving: ')
        depart_now = input('Would you like to depart now? [Y/n]: ')

        travel_information = {'start_address': start_address, 'end_address': end_address, 'travel_mode': travel_mode, 'depart_now': depart_now}

        return travel_information
