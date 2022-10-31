# PySuit
A unified collection of python functions  eg dictsort,nested_iterator etc

#### Purpose of the Package
+ The purpose of the package is to provide a collection of fuction and module indices in one unified libary


### Features
+  Collection of PySuit
   -  DictCollection
   -  NestedCollections
   -  ExcludeRandom
   -  DataTypeCollection
+  Collection of DictCollection
   -  dictsort
   -  dict_key_searching
   -  etc
+  Collection of NestedCollections
   -  nested_iterator
   -  etc
+  Collection of ExcludeRandom
   -  exclude_random
   -  etc
+  Collection of DataTypeCollection
   -  fake_random_datatype
   -  etc

### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation
```bash
pip install pysuit
```
### Usage
Using the short forms or abbreviated forms of indices
### DictCollections
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort(dictionary , flag)

dict_collection.dict_key_searching(dictionary, key)

```

#### Examples of DictCollections
```python
from pysuit import DictCollections
```
```python
dict_collection = DictCollections()
```
```python
dict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)
```
```python
Sorted Dictionary is => {1: 64, 'a': 34, 'b': 3, 67: 'c'}
```
```python
dict_collection.dict_key_searching({'a': {1: {'r':'v'}, 'i': '22'}, 'D': {'a': 'J', 22: 2}} , a)
```
```python
Resultant Dictionary is => ({1: {'r': 'v'}, 'i': '22'}, 'J')
```
### NestedCollections
```python
from pysuit import NestedCollections

nested_collection = NestedCollections()

nested_collection.nested_iterator(nested_list)
```
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
### ExcludeRandom
```python
from pysuit import ExcludeRandom

exclude_random = ExcludeRandom()

exclude_random.exclude_random(start, stop, [exclude numbers])

```
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
### DataTypeCollection
```python
from pysuit import DataTypeCollection

data_collection = DataTypeCollection()

data_collection.fake_random_datatype(datatype, length of datatype)
```
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
### Contribution
Contributions are welcome
Notice a bug let us know. Thanks


### Author
+ Main Maintainer: Deepak Patidar / Nitesh Yadav
+ Team Thoughtwin

### License
+ MIT