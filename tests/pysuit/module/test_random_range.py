# -*- coding: utf-8 -*-
import pytest
from faker import Faker
from pysuit.modules.exclude_random import ExcludeRandom
from pysuit.interface import PySuit

class TestExcludeRandom():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def random_exclude(self):

        random_exclude = ExcludeRandom()
        return random_exclude

    def test_name(self, random_exclude):

        assert random_exclude.__name__ == "pysuit.ExcludeRandom()"

    def test_object_of_type_random_exclude(self, random_exclude):

        assert isinstance(random_exclude, PySuit)


    def test_passes_with_no_start(self, fake, random_exclude):
        start = None
        stop = fake.random_int()
        number_of_excludes = fake.random_int()
        
        with pytest.raises(Exception):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_passes_with_no_stop(self, fake, random_exclude):
        start = fake.random_int()
        stop = None
        number_of_excludes = fake.random_int()

        with pytest.raises(Exception):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_passes_with_no_number_of_excludes(self, fake, random_exclude):
        start = fake.random_int()
        stop = fake.random_int()
        number_of_excludes = None
        with pytest.raises(Exception):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_passes_with_valid_exclude_random_number(self, fake, random_exclude):
        start = fake.random_int()
        stop = fake.random_int()
        number_of_excludes = fake.random_int()
        
        result = random_exclude.exclude_random(self, fake, number_of_excludes)
        print(result)
