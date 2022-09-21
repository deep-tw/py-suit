# -*- coding: utf-8-*-
"""
###### exclude random #######
## Version 0.1 ##

# ---- List of fuctions -----
# exclude_random = this function is work for exluding the number and print random number.
"""

import logging
from pysuit.interface import PySuit
from random import choice

class ExcludeRandom(PySuit):
    
    """
    except exclude generate random number.
    """

    __name__ = "pysuit.ExcludeRandom()"

    
    def exclude_random(self, start, stop, number_of_excludes):
        """
        this function is work for excluding the number given by the user and generate a random number between the range.
        
        """
        
        try:
            exclude_number_list = []
            if stop > start and number_of_excludes <= ((stop-start)-1):
                for number in range(number_of_excludes):
                    exclude_number  = int(input("enter the excluded number "+str(number+1)+":"))
                    if (exclude_number>=start) and (exclude_number <= stop):
                        exclude_number_list.append(exclude_number)
                    else:
                        raise Exception("Enter a valid number which belongs to the start and stop range")
            else:
                raise Exception("please enter the valid number which belongs to range")     
                        
            return choice(list(set(range(start, stop)) - set(exclude_number_list)))
                
            
        except Exception as e:
            raise e

