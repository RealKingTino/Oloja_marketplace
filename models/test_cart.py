#!/usr/bin/python3
"""This module contains the User class"""
from cart import Cart
from product import Product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()

product1 = Product(name="Product 1", price=10)
product2 = Product(name="Product 2", price=15)

cart.add_item(product1, quantity=2)
cart.add_item(product2)

print("Cart Contents:")
for product, quantity in cart.items.items():
    print(f"Product: {product.name}, Price: {product.price}, Quantity: {quantity}")

total_price = cart.calculate_total_price()
print("\nTotal Price:", total_price)

cart.remove_item(product1, quantity=1)

print("\nUpdated Cart Contents:")
for product, quantity in cart.items.items():
    print(f"Product: {product.name}, Price: {product.price}, Quantity: {quantity}")
