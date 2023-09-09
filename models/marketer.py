#!/usr/bin/python3
"""Defines the Marketer class."""
from models.base_model import BaseModel


class Marketer(BaseModel):
    """This class defines the marketer object"""
        self.name = name
        self.contact_info = contact_info
        self.products_for_sale = []
        self.sales_history = []

    def upload_product(self, product):
        """
        Upload a new product for sale.
        """
        self.products_for_sale.append(product)

    def manage_product(self, product_id, updated_product_data):
        """
        Update an existing product's details.
        """
        for product in self.products_for_sale:
            if product.id == product_id:
                product.update(updated_product_data)
                break

    def delete_product(self, product_id):
        """
        Delete a product from the list of products for sale.
        """
        self.products_for_sale = [product for product in self.products_for_sale if product.id != product_id]

    def view_sales_history(self):
        """
        View sales history and statistics.
        """
        return self.sales_history
