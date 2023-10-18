#!/usr/bin/python3
"""This module contains the User class"""
from .base_model import BaseModel

class User(BaseModel):
    """This class define the user"""
    username = ""
    email = ""
    user_id = ""
    password = ""
    shipping_address = ""
    payment_info = ""


    def update(self, **kwargs):
        """this method is used to update the users information"""
        first_key = list(kwargs)[0]
        value = kwargs[first_key]
        is_owner = autenticate(self)
        if is_owner == True:
            if first_key == password:
                add_password()
                #encrypted_pwd = encrypt(value)
                #setattr(self, password, value)
            elif first_key == email:
                add_email()

            elif first_key == shipping_address:
                add_shipping_address()

            elif first_key == payment_info:
                add_payment_info()

            elif first_key == username:
                self.username == value
                #add_username()
