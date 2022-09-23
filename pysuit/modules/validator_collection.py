# -*- coding: utf-8-*-
import re

"""
validators for email or mobile number
"""
# ---- List of fuctions -----


class Validators():
    """
        validators for email or mobile number

    """
    __name__ = "pysuit.Validators()"
    """
        created function ===> validate_email
    """
    output = []

    def email_validation(self, email_address):

        """
        function used for validating email
        """
        """
        Make a regular expression
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        try:
            if email_address == "":
                raise Exception('Enter email address')

            elif(re.fullmatch(regex, email_address)):
                return  email_address

            else:

                raise Exception("Invalid email")

        except Exception as e:

            raise e
        

    """
    Python program to check  given mobile number is valid  or not
    """

    def mobile_validator(self, mobile_no):

        try:


            r=re.fullmatch('[6-9][0-9]{9}',mobile_no) 

            if r!=None:  
                return mobile_no

            elif mobile_no == "":

                raise Exception("Plese Enter mobile Number")

            else:

                raise Exception(' Not a Valid Mobile Number')

        except Exception as e :
            raise e
