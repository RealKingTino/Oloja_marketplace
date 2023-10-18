#!/usr/bin/python3
"""This module contains the User class"""
from marketer import Marketer

# Define a simple Product class for testing purposes
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Create a Marketer instance
marketer = Marketer("John Doe", "john@example.com")

# Create some product instances
product1 = Product(id=1, name="Product 1", price=10)
product2 = Product(id=2, name="Product 2", price=15)

# Upload products
marketer.upload_product(product1)
marketer.upload_product(product2)

# View products for sale
print("Products for sale:")
for product in marketer.products_for_sale:
    print(f"Product: {product.name}, Price: {product.price}")
