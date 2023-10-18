#!/usr/bin/python3
"""This module contains the Order class"""
from models.base_model import BaseModel

class Order(BaseModel):
    """This class detines an oder object"""
    products = []
    total_price = 0
    no_of_product = 0
    status = ""
    shiping_details = ""

    def create(self, items=[]):
        """This method creates an order"""
        for item in items:
            product.append(item)
            no_of_product += 1
            total_price += item.price

        if len(product) > 0:
            status = "pending"

    def deliverd(self):
        """confairm when order.is derlivered"""
        status = "deliverd"
