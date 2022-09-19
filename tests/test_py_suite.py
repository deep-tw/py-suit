# -*- coding: utf-8 -*-
import pytest
from unittest.mock import Mock, patch
from faker import Faker
from pysuit.modules.dict_collection import DictCollections
from pysuit import __version__

class TestPySuit():
        
    @pytest.fixture
    def fake(self):
        return Faker()

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_dictionary_arg(self, fake):
        self.dictionary = {}
        for number in range(10):
            key = fake.word()
            value = fake.random_int()
            self.dictionary.update({key: value})
        
    
        dic = self.dictionary
        res = dic.keys()
        obj = DictCollections()
        result = obj.dictsort(dic, "values")
        res1 = dic.keys()

        assert dic == result
