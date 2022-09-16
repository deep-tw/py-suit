# -*- coding: utf-8 -*-

from pysuit import PySuit


pysuit = PySuit()

a = {"": 12, 6: 'd', 'b': 3, 'a': 34, 67: 'c', 1: 64}
# a = []
flag = ""
res = pysuit.dictsort(a, flag)
print(res)
