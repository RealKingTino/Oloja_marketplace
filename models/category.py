#!/usr/bin/python3
"""describe a category instance"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Category(BaseModel, Base):
    """defines a Category instance"""
    __tablename__ = "category"

    name = Column(String(128), nullable=False)
    description = Column(String(256))
    products = relationship('Product', backref='category', cascade="all, delete")

    def add_product(self, product):
        """Adds a product to the category."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the category."""
        if product in self.products:
            self.products.remove(product)

    def get_products(self):
        """Retrieves all products associated with the category."""
        return self.products

    def update_name(self, new_name):
        """Updates the name of the category."""
        self.name = new_name

    def update_description(self, new_description):
        """Updates the description of the category."""
        self.description = new_description

    def get_category_info(self):
        """Retrieves information about the category."""
        return f"Category: {self.name}\nDescription: {self.description}"

    def delete_category(self):
        """Deletes the category from the database."""
        dbstorage.delete(self)
        dbstorage.save()
