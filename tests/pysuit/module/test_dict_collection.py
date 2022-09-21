# -*- coding: utf-8 -*-
import pytest
from faker import Faker
from pysuit.modules.dict_collection import DictCollections
from pysuit.interface import PySuit


class TestDictCollection():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def dict_collection(self):

        dict_collection = DictCollections()
        return dict_collection

    def test_name(self, dict_collection):

        assert dict_collection.__name__ == "pysuit.DictCollections()"

    def test_object_of_type_dict_collection(self, dict_collection):

        assert isinstance(dict_collection, PySuit)

    def test_passes_with_no_flag(self, fake, dict_collection):
        input_dict = {
            fake.word(): fake.random_int(),
            fake.word(): fake.word(),
            fake.word(): fake.pyfloat(),
            fake.word(): fake.pyfloat(),
            fake.word(): fake.word(),
        }

        result = dict_collection.dictsort(input_dict)

        assert result == input_dict

    def test_failed_with_invaild_dict(self, fake, dict_collection):

        input_dict = [
            fake.random_int(),
            fake.word(),
            fake.pyfloat(),
            fake.pyfloat(),
            fake.word(),
        ]

        with pytest.raises(AttributeError):
            dict_collection.dictsort(input_dict)

    def test_failed_with_no_input_dict(self, fake, dict_collection):

        with pytest.raises(TypeError):
            dict_collection.dictsort()

    def test_passes_with_valid_dictionary_and_flag(self, fake, dict_collection):

        input_dict = {
            fake.word(): fake.random_int(),
            fake.word(): fake.word(),
            fake.word(): fake.pyfloat(),
            fake.word(): fake.pyfloat(),
            fake.word(): fake.word(),
        }

        result = dict_collection.dictsort(input_dict, "values")

        assert result == input_dict
