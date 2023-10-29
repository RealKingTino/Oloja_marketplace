#!/usr/bin/python3
"""This module contains the Order class"""
from models.base_model import BaseModel, Base
from models import Column, String, Integer
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """This class detines an oder object"""
    __tablename__ = "orders"

    products = Column(String(60), nullable=False)
    total_price = Column(Integer, nullable=False)
    no_of_product = Column(Integer, nullable=False)
    status = Column(String(60), nullable=False, default="pending")
    shiping_details = Column(String(60), nullable=False)

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
