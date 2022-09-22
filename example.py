# from pysuit import DictCollections
# from pysuit import ExcludeRandom
# from pysuit import NestedCollections
from pysuit import DataTypeCollection

# d = DictCollections()

# a = {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}

# flag = "keys"
# res = d.dictsort(a, flag)

# print(res)

# st = 100
# en = 200
# ex = [2, 4, 5, 6, 8]
# obj = ExcludeRandom()
# res = obj.exclude_random(st, en, ex)
# print(res)
# lst = ('a', ['bb', ('ccc', 'ddd'), 'ee', 'ff'], 'g', 'h')
# obj = NestedCollections()
# res = obj.removNestings(lst)
# print(res)

obj = DataTypeCollection()
print(obj.fake_random_datatype(set, 10))