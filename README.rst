PySuit
======

|Read the Docs| |codecov| |PyPI version|

A unified collection of python functions eg dictsort,nested_iterator etc

Purpose of the Package
----------------------

-  The purpose of the package is to provide a collection of fuction and
   module indices in one unified libary

Documentation
-------------

-  The official documentation is hosted on readthedocs.io:
   https://py-suit.readthedocs.io/en/latest/

Features
--------

-  Collection of PySuit

   -  DictCollection
   -  NestedCollections
   -  ExcludeRandom
   -  DataTypeCollection

-  Collection of DictCollection

   -  dictsort
   -  etc

-  Collection of NestedCollections

   -  nested_iterator
   -  etc

-  Collection of ExcludeRandom

   -  exclude_random
   -  etc

-  Collection of DataTypeCollection

   -  fake_random_datatype
   -  etc ### Getting Started The package can be found on pypi hence you
      can install it using pip

Installation
~~~~~~~~~~~~

.. code:: bash

   pip install pysuit

Usage
-----

Using the short forms or abbreviated forms of indices

DictCollection
--------------

.. code:: python

   from pysuit import DictCollections

   dict_collection = DictCollections()

   dict_collection.dict_sort(dictionary , flag)

Examples of DictCollections
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from pysuit import DictCollections

.. code:: python

   dict_collection = DictCollections()

.. code:: python

   dict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)

.. code:: python

   Sorted Dictionary is => {1: 64, 'a': 34, 'b': 3, 67: 'c'}

NestedCollections
-----------------

.. code:: python

   from pysuit import NestedCollections

   nested_collection = NestedCollections()

   nested_collection.nested_iterator(nested_list)

Examples of NestedCollections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from pysuit import NestedCollections

.. code:: python


   nested_collection = NestedCollections()

.. code:: python

   nested_collection.nested_iterator([[0, 4], [2, 3, 4], [0, 1, 2], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])

.. code:: python

   Converted list is => [0, 4, 2, 3, 4, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

ExcludeRandom
-------------

.. code:: python

   from pysuit import ExcludeRandom

   exclude_random = ExcludeRandom()

   exclude_random.exclude_random(start, stop, [exclude numbers])

Examples of ExcludeRandom
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from pysuit import ExcludeRandom

.. code:: python

   exclude_random = ExcludeRandom()

.. code:: python

   exclude_random.exclude_random(1, 10, [4, 5, 9])

.. code:: python

   Random number is => 8

DataTypeCollection
------------------

.. code:: python

   from pysuit import DataTypeCollection

   data_collection = DataTypeCollection()

   data_collection.fake_random_datatype(datatype, length of datatype)

Examples of DataTypeCollection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from pysuit import DataTypeCollection

.. code:: python

   data_collection = DataTypeCollection()

.. code:: python

   data_collection.fake_random_datatype(list, 10)

.. code:: python

   Fake random data is => [93, 91, 9163, -1967.88203, 3, 'thousand', -197247.03, 913, 983, 'thousand']

Contribution
------------

Contributions are welcome Notice a bug let us know. Thanks

Author
------

-  Main Maintainer: Avinash Tiwari
-  Team Thoughtwin

License
-------

-  MIT

.. |Read the Docs| image:: https://readthedocs.org/projects/py-suit/badge/?version=latest
   :target: py-suit.rtfd.io/en/latest/
.. |codecov| image:: https://codecov.io/github/deep-tw/py-suit/branch/release/graph/badge.svg?token=WR57HD3UTR
   :target: https://codecov.io/github/deep-tw/py-suit
.. |PyPI version| image:: https://badge.fury.io/py/pysuit.svg
   :target: https://badge.fury.io/py/pysuit
