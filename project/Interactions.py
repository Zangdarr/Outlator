# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 14:22:34 2015

@author: alexandre Verkyndt
"""

class Interactions_with_user:

    def __init__(self):
        '''
        Empty        
        '''

    def choose_your_mode(self):
        '''
        Ask the user about the action he want to do : edition or reading.
        '''
        print('Choose between edition mode or reading mode (e/r)')
        while(True):  
            mode = input('Your choice :')
            if( mode !='e' and mode !='r' and             \
                mode !='edition' and mode !='reading' and \
                mode !='edit' and mode !='read'):
                    
                print('Error : please choose in e/edit/edition or r/read/reading')
                continue
            break
        return mode[0]


class Interactions_with_database:
    
    def __init__(self):
        '''
        Empty
        '''
