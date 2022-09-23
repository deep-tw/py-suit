# -*- coding: utf-8 -*-
from random import sample
import pytest
from faker import Faker
from pysuit.modules.validator_collection import Validators
from pysuit.interface import PySuit


class TestValidators():

    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def validators(self):

        validators = Validators()
        return validators

    def test_name(self, validators):

        assert validators.__name__ == "pysuit.Validators()"

    def test_object_of_type_of_validators(self, validators):
    
        assert isinstance(validators, PySuit)

    def test_failed_with_no_input_email(self, validators):

        with pytest.raises(TypeError):
            validators.email_validation()

    def test_passes_with_valid_email(self, fake, validators):

        sample_email=fake.email()
        
        result = validators.email_validation(sample_email)
        
        assert result == sample_email


    def test_passes_empty_email_address(self, fake, validators):

        sample_email = ""
        with pytest.raises(Exception):
            validators.email_validation(sample_email)


    def test_failed_with_no_input_mobile_number(self, validators):

        with pytest.raises(TypeError):
            validators.mobile_validator()

    def test_passes_with_valid_mobile_number(self, fake, validators):
        
        sample_mobile='7898525961'
        
        result = validators.mobile_validator(sample_mobile)
        
        assert result == sample_mobile


    def test_passes_empty_mobile_number(self, fake, validators):

        sample_mobile = ""

        with pytest.raises(Exception):
            validators.mobile_validator(sample_mobile)

