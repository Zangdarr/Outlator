# -*- coding: utf-8 -*-
"""
@author: alexandre Verkyndt
"""

import Interactions

def mode_launcher(self, mode):
    print("The mode you choosed will be launch.\n\n")

def edition_mode(self):
    print("You are in the edition mode.\n\n")

def reading_mode(self):
    print("You are in the reading mode.\n\n")
    
if __name__ == '__main__':
    
    to_user = Interactions.Interactions_with_user()
    
    mode = to_user.choose_your_mode()
    print('You choosed : ' + mode)
    