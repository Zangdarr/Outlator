# -*- coding: utf-8 -*-
"""
@author: alexandre Verkyndt
"""

import Interactions

def mode_launcher(mode):
    print("The mode you choosed will be launch.\n\n")


    
if __name__ == '__main__':
    
    to_user = Interactions.Interactions_with_user()
    
    mode = to_user.choose_your_mode()
    print('You choosed : ' + mode)
    