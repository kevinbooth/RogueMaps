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

        start_address = input('\nPlease enter the starting address including all nessesary information in the format as follows.\n (ex: 88 Commercial St, Manchester, NH 03101):\n')

        end_address = input('\nPlease enter the starting address including all nessesary information in the format as follows.\n (ex: 88 Commercial St, Manchester, NH 03101):\n')

        travel_mode = input('\nPlease choose from the following travel modes: walking, bicycling, transit, or driving:\n')
        correctbool=False
        while correctbool == False:
            err = 0
            for a in tMode:
                if travel_mode != a:
                    err+=1
                    if err >= 4:
                        print('\nThe mode of travel you have entered does not match any of the options.\n')
                        travel_mode = input('Please enter one the following travel modes: WALKING, BICYCLING, TRANSIT, or DRIVING: \n')

                else:
                    correctbool = True

        depart_now = input('\nWould you like to depart now? [y/n]: \n')
        correctbool = False
        while correctbool == False:
            if depart_now != 'y' and depart_now != 'n':
                print('\nInvalid response! Please enter \'y\' for \'yes\' or \'n\' for \'no.\'\n')
                depart_now = input('\nWould you like to depart now? [y/n]: \n')
            else:
                correctbool = True

        travel_information = {'start_address': start_address, 'end_address': end_address, 'travel_mode': travel_mode, 'depart_now': depart_now}

        return travel_information
