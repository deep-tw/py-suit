# -*- coding: utf-8 -*-
import pytest
from faker import Faker
from pysuit.modules.validator_collections import ValidatorCollection


class TestValidators():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def validators(self):

        validators = ValidatorCollection()
        return validators

    def test_name(self, validators):

        assert validators.__name__ == "pysuit.ValidatorCollection()"

    def test_failed_with_no_input_email(self, validators):

        with pytest.raises(TypeError):
            validators.email_validation()

    def test_passes_with_valid_email(self, fake, validators):

        sample_email = fake.email()
        result = validators.email_validation(sample_email)
        assert result == sample_email

    def test_passes_empty_email_address(self, fake, validators):

        sample_email = ""
        with pytest.raises(Exception):
            validators.email_validation(sample_email)

    def test_passes_invalid_email_address(self, fake, validators):

        sample_email = "d"
        with pytest.raises(Exception):
            validators.email_validation(sample_email)

    def test_failed_with_no_input_mobile_number(self, validators):

        with pytest.raises(TypeError):
            validators.mobile_validator()

    def test_passes_with_valid_mobile_number(self, fake, validators):

        sample_mobile = '7898545961'
        result = validators.mobile_validator(sample_mobile)
        assert result == sample_mobile

    def test_passes_empty_mobile_number(self, fake, validators):

        sample_mobile = ""
        with pytest.raises(Exception):
            validators.mobile_validator(sample_mobile)

    def test_passes_invalid_mobile_number(self, fake, validators):

        sample_mobile = "545"
        with pytest.raises(Exception):
            validators.mobile_validator(sample_mobile)
