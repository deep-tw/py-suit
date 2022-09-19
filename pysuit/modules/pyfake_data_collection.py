# -*- coding: utf-8-*-
"""
###### Dict Collections #######
## Version 0.1 ##

# ---- List of fuctions -----
# 
"""
from faker import Faker
import random
import logging
from pysuit.interface import PySuit



class PyfakeDataCollection(PySuit):
    """
    List of fake data collections
    """

    __name__ = "pysuit.PyfakeDataCollection()"

    def fakedata(self, data_type, size):
        fake = Faker()
        random_list = [fake.word(), fake.pyfloat(), fake.random_int()]

        if data_type is dict:
            final_dict = {}
            for lenght in range(size):
                key = random.choice(random_list)
                value = random.choice(random_list)
                final_dict.update({key: value})
            return final_dict

        if data_type is list:
            final_list = []
            for lenght in range(size):
                item = random.choice(random_list)
                final_list.append(item)
            return final_list

        if data_type is set:
            final_set = set()
            for lenght in range(size):
                item = random.choice(random_list)
                final_list.add(item)
            return final_set



