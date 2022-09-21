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


    def test_failed_with_no_input_nested_list(self, fake, nested_list ):

        with pytest.raises(TypeError):
            nested_list.removNestings()


    def test_passes_with_valid_nested_list(self, fake, nested_list):

        sample_list = [
            fake.random_int(),[
                fake.random_int(),fake.word(),fake.random_int()
                ],
            fake.word(),fake.random_int(),[
                fake.random_int(),[
                    fake.word(),fake.random_int()
                    ]
                ]
        ]

        result = nested_list.removNestings(sample_list)
        print(result)
        assert result != sample_list


    def test_passes_with_invalid_nested_list_input_type(self, fake, nested_list):

        sample_list = []
        print(sample_list)

        result= nested_list.removNestings(sample_list)
        print(result)
        
        assert len(result) != 0 , "the list is non empty"



    def test_passes_with_valid_tuple(self, fake, nested_list):

        sample_set=(
            fake.random_int(),
            fake.random_int(),
            fake.random_int(),
            fake.random_int(),
            (fake.pyfloat(),(fake.word()),
            fake.word(), 
            (fake.random_int(),fake.random_int(),fake.random_int())),
            {fake.random_int():fake.word()})

        result = nested_list.removNestings(sample_set)

        assert result != sample_set


    def test_passes_with_valid_dict(self, fake, nested_list):

        sample_dict= {
                fake.random_int(): fake.word(),
                fake.random_int():fake.word(),
                fake.random_int():{fake.word():fake.word(), 
                fake.word():{fake.word():{fake.word():fake.word()}}}}

        result = nested_list.removNestings(sample_dict)

        assert result != sample_dict



