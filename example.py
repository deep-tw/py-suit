from pysuit import DictCollections

d = DictCollections()

a = {"b": 3, "a": 34, 67: "c", 1: 64}

flag = ""
res = d.dictsort(a, flag)

print(res)
