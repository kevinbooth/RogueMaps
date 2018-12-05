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
        print('Welcome to RogueMaps where you can save your ' +
              'directions into a PDF')

    def retrieve_user_data():
        """
        Retrieves data about directions from the user
        Returns: dictionary with the following keys:
            start_address
            end_address
            depart_now
        """
        t_mode = {'walking': 1, 'bicycling': 2, 'transit': 3, 'driving': 4}

        start_address = input('\nPlease enter the starting address including' +
                              ' all nessesary information in the format as ' +
                              'follows.\n(ex: 88 Commercial St, Manchester,' +
                              ' NH 03101):\n')
        end_address = input('\nPlease enter the end address including' +
                            ' all nessesary information in the format' +
                            ' as follows.\n(ex: 88 Commercial St,' +
                            ' Manchester, NH 03101):\n')
        travel_mode = input('\nPlease choose from the following travel' +
                            ' modes: walking, bicycling, transit,' +
                            ' or driving:\n')
        correct_bool = False
        while correct_bool is False:
            err = 0
            for a in t_mode:
                if travel_mode != a:
                    err += 1
                    if err >= 4:
                        print('\nThe mode of travel you have entered does' +
                              ' not match any of the options.\n')
                        travel_mode = input('Please enter one the following' +
                                            ' travel modes: WALKING,' +
                                            ' BICYCLING, TRANSIT,' +
                                            ' or DRIVING: \n')
                else:
                    correct_bool = True

        depart_now = input('\nWould you like to depart now? [y/n]: \n')
        correct_bool = False
        while correct_bool is False:
            if depart_now != 'y' and depart_now != 'n':
                print('\nInvalid response! Please enter \'y\' for \'yes\'' +
                      ' or \'n\' for \'no.\'\n')
                depart_now = input('\nWould you like to depart now? [y/n]: \n')
            else:
                correct_bool = True

        travel_info = {'start_address': start_address,
                       'end_address': end_address, 'travel_mode': travel_mode,
                       'depart_now': depart_now}

        return travel_info
