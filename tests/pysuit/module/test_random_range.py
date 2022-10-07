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

    def test_failed_with_no_stop(self, fake, random_exclude):
        start = fake.random_int()
        stop = None
        number_of_excludes = fake.random_int()

        with pytest.raises(Exception):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_failed_with_no_number_of_excludes(self, fake, random_exclude):
        start = fake.random_int()
        stop = fake.random_int()
        number_of_excludes = None
        with pytest.raises(Exception):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_passes_with_exclude_random_number(self, fake, random_exclude):

        random_number = fake.random_int()
        number_of_excludes = [
            fake.random_int(1, 10),
            fake.random_int(1, 10),
            fake.random_int(1, 10),
            fake.random_int(1, 10),
            fake.random_int(1, 10)
        ]
        start = min(number_of_excludes) - 1
        stop = max(number_of_excludes) + 1

        result = random_exclude.exclude_random(start, stop, number_of_excludes)

        assert random_number != result

    def test_failed_with_invalid_start_stop(self, fake, random_exclude):
        start = 5
        stop = 1
        number_of_excludes = fake.random_int()

        with pytest.raises(ValueError):
            random_exclude.exclude_random(start, stop, number_of_excludes)

    def test_failed_with_invalid_number(self, fake, random_exclude):
        start = 1
        stop = 5
        number_of_excludes = [10, 20]

        with pytest.raises(ValueError):
            random_exclude.exclude_random(start, stop, number_of_excludes)
