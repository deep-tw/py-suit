# -*- coding: utf-8-*-
"""
###### exclude random #######
## Version 0.1 ##

# ---- List of fuctions -----
# exclude_random = this function is work for
exluding the number and print random number.
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
        this function is work for excluding the number given by
        the user and generate a random number between the range.

        """
        try:
            exclude_number_list = []
            if stop > start and len(number_of_excludes) <= ((stop-start)-1):
                for number in number_of_excludes:
                    if (number >= start) and (number <= stop):
                        exclude_number_list.append(number)
                    else:
                        raise Exception
                        ("Enter valid number belongs start and stop range")
            else:
                raise Exception
                ("please enter the valid number which belongs to range")

            return
            choice(list(set(range(start, stop)) - set(exclude_number_list)))
        except Exception as e:
            raise e
