
# -*- coding: utf-8 -*-
import pytest
import random
from faker import Faker
from pysuit.modules.random_datatype_collection import DataTypeCollection
from pysuit.interface import PySuit


class TestDataTypeCollection():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def random_collection(self):

        random_collection = DataTypeCollection()
        return random_collection

    def test_name(self, random_collection):

        assert random_collection.__name__ == "pysuit.DataTypeCollection()"

    def test_object_of_type_random_collection(self, random_collection):

        assert isinstance(random_collection, PySuit)

    def test_passes_with_no_datatype(self, fake, random_collection):

        random_data_type = None
        data_type = None
        size = fake.random_int()
        result = random_collection.fake_random_datatype(data_type, size)
        assert random_data_type == result

    def test_passes_with_no_size(self, fake, random_collection):

        datatype = list
        size = None
        with pytest.raises(Exception):
            random_collection.fake_random_datatype(datatype, size)

    def test_passes_with_zero_size(self, fake, random_collection):

        random_list = list
        result = random_collection.fake_random_datatype(random_list, 0)
        assert type(result) == random_list

    def test_pass_with_valid_datatype_and_size(self, fake, random_collection):

        random_list = [fake.word(), fake.pyfloat(), fake.random_int()]
        random_data_type = {
            fake.random_int(): random.choice(random_list),
            fake.random_int(): random.choice(random_list),
            fake.random_int(): random.choice(random_list),
            fake.random_int(): random.choice(random_list),
            fake.random_int(): random.choice(random_list),
        }
        size = len(random_data_type)
        result = random_collection.fake_random_datatype(dict, size)
        assert len(random_data_type) == len(result)
