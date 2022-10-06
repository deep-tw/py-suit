### Usage
Using the short forms or abbreviated forms of indices

### DictCollections
```python
from pysuit import DictCollections

dict_collection = DictCollections()

dict_collection.dict_sort(dictionary , flag)

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