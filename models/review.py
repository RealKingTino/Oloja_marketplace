#!/usr/bin/python3
"""describe a review instance"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """defines a Category instance"""
    __tablename__ = "review"

    text = Column(String(1000), nullable=False)
    rating = Column(Integer, nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, text, rating, product_id, user_id):
        """
        Initializes a Review instance with the provided parameters
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.product_id = product_id
        self.user_id = user_id
