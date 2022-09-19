PySuit
======

A unified collection of python functions eg dictsort,nested_iterator etc

Purpose of the Package
----------------------

-  The purpose of the package is to provide a collection of fuction and
   module indices in one unified libary

Features
--------

-  Collection of PySuit

   -  DictCollection
   -  ListCollection
   -  etc

-  Collection of DictCollection

   -  dictsort
   -  etc

-  Collection of ListCollection

   -  nested_iterator
   -  etc

Getting Started
---------------

The package can be found on pypi hence you can install it using pip

Installation
~~~~~~~~~~~~

.. code:: bash

   pip install pysuit

Usage
-----

Using the short forms or abbreviated forms of indices

.. code:: python

   from pysuit import DictCollections

   dict_collection = DictCollections()

   dict_collection.dict_sort(dictionary , flag)

Examples
~~~~~~~~

.. code:: python

   from pysuit import DictCollections

.. code:: python

   dict_collection = DictCollections()

.. code:: python

   dict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)

.. code:: python

   Sorted Dictionary is => {1: 64, 'a': 34, 'b': 3, 67: 'c'}

Contribution
------------

Contributions are welcome Notice a bug let us know. Thanks

Author
------

-  Main Maintainer: Deepak Patidar / Nitesh Yadav
-  Team Thoughtwin

License
-------

-  MIT
