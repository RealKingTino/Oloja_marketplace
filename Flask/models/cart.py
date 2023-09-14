#!/usr/bin/python3
"""Defines the Cart class."""
from .base_model import BaseModel
from models import db, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Cart(db.Model, BaseModel):
    """This class defines a cart object"""
    __tablename__ = "carts"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="cart")

    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_item(self, product, quantity=1):
        """
        Add a product to the cart with the specified quantity.
        """
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity=1):
        """
        Remove a specified quantity of a product from the cart.
        If the quantity reaches zero, the product is removed from the cart.
        """
        if product in self.items:
            self.items[product] -= quantity
            if self.items[product] <= 0:
                del self.items[product]

    def calculate_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.price * quantity
        return total_price