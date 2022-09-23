# PySuit

[![Read the Docs](https://readthedocs.org/projects/py-suit/badge/?version=latest)](py-suit.rtfd.io/en/latest/) [![codecov](https://codecov.io/github/deep-tw/py-suit/branch/release/graph/badge.svg?token=WR57HD3UTR)](https://codecov.io/github/deep-tw/py-suit)

A unified collection of python functions  eg dictsort,nested_iterator etc

#### Purpose of the Package
+ The purpose of the package is to provide a collection of fuction and module indices in one unified libary


### Features
+ Collection of PySuit
	- DictCollection
	- ListCollection
	- etc 
+ Collection of DictCollection
	- dictsort
    - etc 
+ Collection of ListCollection
    - nested_iterator
    - etc 




### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation
```bash
pip install pysuit
```


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

### Contribution
Contributions are welcome
Notice a bug let us know. Thanks


### Author
+ Main Maintainer: Deepak Patidar / Nitesh Yadav
+ Team Thoughtwin

### License
+ MIT
