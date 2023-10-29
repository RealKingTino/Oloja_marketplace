#!/usr/bin/python3
"""This module contains the User class"""
from .base_model import BaseModel, Base
from models import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class define the user"""
    __tablename__ = "users"

    user_name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    shipping_address = Column(String(256), nullable=False)
    payment_info = Column(String(256), nullable=False)
    cart = relationship('Cart', backref='user', cascade="all, delete")

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
