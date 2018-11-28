"""
user.py
Module that provides user specific functions
Created by Kevin Booth
Nov 15, 2018
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

        tMode = {'walking':1, 'bicycling':2, 'transit':3, 'driving':4}
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
        correctbool=False
        while correctbool == False:
            err = 0
            for a in tMode:
                if travel_mode != a:
                    err+=1
                    if err >= 4:
                        print('The mode of travel you have entered does not match any of the options.')
                        travel_mode = input('Please enter one the following travel modes: WALKING, BICYCLING, TRANSIT, or DRIVING: ')

                else:
                    correctbool = True

        depart_now = input('Would you like to depart now? [y/n]: ')
        correctbool = False
        while correctbool == False:
            if depart_now != 'y':
                print('Invalid response! Please enter \'y\' for \'yes\' or \'n\' for \'no.\'\n')
                depart_now = input('Would you like to depart now? [y/n]: ')
            else:
                correctbool = True

        travel_information = {'start_address': start_address, 'end_address': end_address, 'travel_mode': travel_mode, 'depart_now': depart_now}

        return travel_information
