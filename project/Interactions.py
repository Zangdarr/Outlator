# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 14:22:34 2015

@author: alexandre Verkyndt
"""

class Interactions_with_user:
    '''
    This class is the palette of interactions that the system can have with the user.
    '''
    def __init__(self):
        '''
        Empty        
        '''
    
    def generic_choose(self,quantity):
        print("Enter the number from 1 to " + str(quantity) + "\n")
        while(True):
            choice = input("Your choice : ")
            if(not(str.isnumeric(choice))):
                print("The entry is not a numeric. Please choose a number from 1 to "+ str(quantity) + "\n")
                continue
            if(int(choice) < 1 or int(choice) > quantity):
                print("Entry incorrect, please choose a number from 1 to "+ str(quantity) + "\n")
                continue
            break
        
        return choice
        
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


import sqlite3


class Interactions_with_database:
    '''
    This class is the palette of interactions that the system can have with the database.
    '''

    conn = 0
    c = 0
    
    def __init__(self):
        '''
        Empty
        '''
        
        #connection to the database
        self.conn = sqlite3.connect('database.db')
        #recuperation of a "Cursor" to execute SQL commands
        self.c = self.conn.cursor()



    def save_modification(self):
        
        '''
        Valide the modification done.
        '''
        self.conn.commit()

    def close_database(self):
        self.conn.close()

    def generate_database(self):
        '''
        This function will generate the two "main" tables.
        '''
        self.c.execute("CREATE TABLE Mangas (ID_mangas integer primary key, Name_manga varchar unique, Author varchar, Resume varchar)")
        self.c.execute("CREATE TABLE Tomes  (ID_tomes integer primary key, ID_manga integer, Page_number integer, Case_number integer, Bubbles_number integer, Contenu_initial varchar, Contenu_traduction varchar, Commentaires varchar, FOREIGN KEY(ID_manga) REFERENCES Mangas(ID_manga))")
        

    def get_list_manga(self):
        self.c.execute("SELECT * FROM Mangas")
        print(self.c.fetchone())
        
    def create_new_ligne(self, table, parameters, values):
        self.c.execute("SELECT count(ID_mangas) FROM Mangas")
        new_ID = self.c.fetchone()
        #new_ID = new_ID[0] +1
        parameters = ('ID_' + table,) + parameters
        print(parameters)
        query = "INSERT INTO " + table + str(parameters) +  ' VALUES ' + str((new_ID[0],) + values)
        print(query)
        self.c.execute(query)
        