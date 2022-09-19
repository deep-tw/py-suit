###  API Documentation

This documentation gives you  overview of the Pysuit functions and method

+ [DictCollections](#DictCollections)
    + [dictsort](#dictsort)


***DictCollections***<a name="DictCollections"><br>

***dictsort***<a name="dictsort">

---

<!-- :sunglasses: See [UserGuid](userguide.md) -->
User Guide to Kick start a collection

The dict sort function is used to sort the dictionary based on the keys and values
### Usage

Using the short forms or abbreviated forms of indices
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort(dictionary , flag)

```
#### Examples
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)

Output => {1: 64, 'a': 34, 'b': 3, 67: 'c'}

```