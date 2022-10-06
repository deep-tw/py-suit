from pysuit.interface import PySuit
from faker import Faker
import pytest


class TestInterface():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def pysuit(self):

        pysuit = PySuit()
        return pysuit

    def test_name(self, pysuit):

        assert pysuit.__name__ == "pysuit.PySuit()"

    def test_object_of_type__validate_item(self, pysuit):

        assert isinstance(pysuit, PySuit)

    def test_failed_with_item_none(self, pysuit):
        with pytest.raises(ValueError):
            pysuit._validate_item(None)

    def test_failed_with_instance_of_pysuit(self, pysuit):
        with pytest.raises(TypeError):
            pysuit._validate_item(pysuit)