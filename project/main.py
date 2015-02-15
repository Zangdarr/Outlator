# -*- coding: utf-8 -*-
"""
@author: alexandre Verkyndt
"""

import Interactions
import Mode

def mode_launcher(mode):
    print("The mode you choosed will be launch.\n\n")

    if(mode == 'e'):
        mode_class = Mode.Mode_edition()
        mode_class.edition_mode()
    elif(mode == 'r'):
        mode_class = Mode.Mode_reading()
        mode_class.reading_mode()
    else:
        print("The mode you choose don't existing. Aborting.")
    
    print("The program will close.")
        


    
if __name__ == '__main__':
    
    to_user = Interactions.Interactions_with_user()
    
    mode = to_user.choose_your_mode()
    print('You choosed : ' + mode)
    