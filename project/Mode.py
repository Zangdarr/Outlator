# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 16:58:55 2015

@author: alexandre Verkyndt
"""
import Interactions

class Mode_edition:
    #Attribut

    #when @notfinish will be false the program will leave the edition mode    
    notfinish = True
    
    def edition_mode(self):
        print("You are in the edition mode.\n\n")
        #until the user want to leave the edition mode
        while(self.notfinish):
            #the user choose the action he want to do
            action = self.choose_action()
            #run the action
            print(action + "  OK\n")
            self.notfinish = False
        
        
        
class Mode_reading:
    
    def reading_mode(self):
        print("You are in the reading mode.\n\n")