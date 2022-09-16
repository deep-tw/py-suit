# -*- coding: utf-8 -*-
import pytest
from unittest.mock import Mock, patch
from faker import Faker
from pysuit.main import PySuit
from pysuit import __version__


class TestPySuit():
        

    @pytest.fixture
    def fake(self):
        return Faker()

    def test_version(self):
        assert __version__ == '0.1.0'

    def dictionary_arg(self, fake):
        dictionary = {}
        for number in range(10):
            key = fake.word()
            value = fake.random_int()
            dictionary.update({key: value})
        return dictionary

    def test_dict_with_valid_keys_values(self, Mock, dictionary_arg):
        d = Mock(PySuit)
      
       




