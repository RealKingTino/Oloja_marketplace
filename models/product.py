#!/usr/bin/python3
""" Defines the product class """

from .base_model import BaseModel
from models import Column, String, Integer, Float
from models.db_storage import DBStorage


class Product(BaseModel):
    """This class defines a product."""
    __tablename__ = "products"

    location = Column(String(256), nullable=False)
    product_name = Column(String(256), nullable=False)
    description = Column(String(1000), nullable=False)
    image = Column(String(256), nullable=False)
    category = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    def create(self, location, product_name, description,
               image, category, price, stock_quantity):
        """Create a new product."""
        self.location = location
        self.product_name = product_name
        self.description = description
        self.image = image
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def read(self, product_id):
        """Read product details."""
        product = db_storage.get(Product, product_id)
        return product

    def update(self, product_id, **kwargs):
        """Update product details."""
        product = db_storage.get(Product, product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            db_storage.save()
            return product
        return None

    def delete(self, product_id):
        """Delete a product."""
        product = db_storage.get(Product, product_id)
        if product:
            db_storage.delete(product)
            db_storage.save()
            return True
        return False

    def calculate_discount(self, discount_percentage):
        """Calculate the discount on the product price."""
        discounted_price = self.price * (1 - discount_percentage / 100)
        return discounted_price

    def process_payment(self, payment_details):
        """Process the payment for the product."""
        pass
