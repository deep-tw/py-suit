from pysuit import PySuit


pysuit = PySuit()

a = {100: 12, 6: 'd', 'b': 3, 'a': 34, 67: 'c', 1: 64}
flag = "keys"
res = pysuit.dictsort(a, flag)
print(res)
