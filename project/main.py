# -*- coding: utf-8 -*-
"""
@author: alexandre Verkyndt
"""

import Interactions


if __name__ == '__main__':
    
    to_user = Interactions.Interactions_with_user()
    
    mode = to_user.choose_your_mode()
    print('You choosed : ' + mode)
    