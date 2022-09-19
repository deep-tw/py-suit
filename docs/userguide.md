### User Guide

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
