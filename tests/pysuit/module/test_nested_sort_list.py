# -*- coding: utf-8 -*-
import pytest
from faker import Faker
from pysuit.modules.nested_iterator import NestedCollections
from pysuit.interface import PySuit


class TestNestedList():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def nested_list(self):

        nested_list = NestedCollections()
        return nested_list

    def test_name(self, nested_list):

        assert nested_list.__name__ == "pysuit.NestedCollections()"

    def test_object_of_nested_list(self, nested_list):

        assert isinstance(nested_list, PySuit)

    def test_failed_with_no_input_nested_list(self, fake, nested_list):

        with pytest.raises(TypeError):
            nested_list.removNestings()

    def test_passes_with_valid_nested_list(self, fake, nested_list):

        sample_list = [
            fake.random_int(),
            [
                fake.random_int(), fake.word(),
                fake.random_int()
            ],
            fake.word(), fake.random_int(),
            [
                fake.random_int(), [
                    fake.word(), fake.random_int()
                ]
            ]
            ]
        result = nested_list.removNestings(sample_list)
        
        assert result != sample_list

    def test_passes_with_empty_nested_list_input_type(self, fake, nested_list):

        sample_list = []
        result = nested_list.removNestings(sample_list)
        assert sample_list == result

    def test_passes_with_valid_nested_tuple(self, fake, nested_list):

        sample_tuple = (
            fake.random_int(),
            fake.random_int(),
            fake.random_int(),
            fake.random_int(),
            (fake.pyfloat(), (
                fake.word()),
                fake.word(), (
                    fake.random_int(),
                    fake.random_int(),
                    fake.random_int()
                )
            )
        )

        result = nested_list.removNestings(sample_tuple)

        assert result != sample_tuple

    def test_passes_with_valid_nested_set(self, fake, nested_list):

        sample_set = {
                fake.random_int(),
                fake.word(),
                fake.random_int(), fake.word(),
                frozenset([fake.random_int(), fake.random_int()])}

        result = nested_list.removNestings(sample_set)

        assert result != sample_set
