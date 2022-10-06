###  API Documentation

This documentation gives you  overview of the Pysuit functions and method

+ [DictCollections](#DictCollections)
    + [dictsort](#dictsort)

---

+ [NestedCollections](#NestedCollections)
    + [nested_iterator](#nested_iterator)

---

+ [ExcludeRandom](#ExcludeRandom)
    + [exclude_random](#exclude_random)

---

+ [DataTypeCollection](#DataTypeCollection)
    + [fake_random_datatype](#fake_random_datatype)

---
### User Guide to Kick start a collection

The dict sort function is used to sort the dictionary based on the keys and values
### Usage
Using the short forms or abbreviated forms of indices

***DictCollections***<a name="DictCollections"><br>
### DictCollections
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort(dictionary , flag)

```
***dict_sort***<a name="dictsort">
#### Examples
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)

Output => {1: 64, 'a': 34, 'b': 3, 67: 'c'}

```
***NestedCollections***<a name="NestedCollections"><br>
### NestedCollections
The nested list, nested set, nested dict, nested tuple function is used to remove nested
```python
from pysuit import NestedCollections

nested_collection = NestedCollections()

nested_collection.nested_iterator(nested_list)

```
***nested_iterator***<a name="nested_iterator">
#### Examples of NestedCollections
```python
from pysuit import NestedCollections
```
```python
nested_collection = NestedCollections()
```
```python
nested_collection.nested_iterator([[0, 4], [2, 3, 4], [0, 1, 2], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
```
```python
Converted list is => [0, 4, 2, 3, 4, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
```
***ExcludeRandom***<a name="ExcludeRandom"><br>
### ExcludeRandom
This function is used to generate random number but except of given elements of list

```python
from pysuit import ExcludeRandom

exclude_random = ExcludeRandom()

exclude_random.exclude_random(start, stop, [exclude numbers])

```
***exclude_random***<a name="exclude_random">
#### Examples of ExcludeRandom
```python
from pysuit import ExcludeRandom
```
```python
exclude_random = ExcludeRandom()
```
```python
exclude_random.exclude_random(1, 10, [4, 5, 9])
```
```python
Random number is => 8
```
***DataTypeCollection***<a name="DataTypeCollection"><br>
### DataTypeCollection
This function is works for generate fake python datatype data like - list, tuple, set, dict

```python
from pysuit import DataTypeCollection

data_collection = DataTypeCollection()

data_collection.fake_random_datatype(datatype, length of datatype)

```
***fake_random_datatype***<a name="fake_random_datatype">
#### Examples of DataTypeCollection
```python
from pysuit import DataTypeCollection
```
```python
data_collection = DataTypeCollection()
```
```python
data_collection.fake_random_datatype(list, 10)
```
```python
Fake random data is => [93, 91, 9163, -1967.88203, 3, 'thousand', -197247.03, 913, 983, 'thousand']
```
