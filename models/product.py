from .base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, text, Integer, Float


class Product(BaseModel, Base):
    """This class defines a product."""
    __tablename__ = "products"
    

    location = Column(String(256), nullable=False)
    product_name = Column(String(256), nullable=False)
    description = Column(String(1000), nullable=False)
    image = Column(String(256), nullable=False)
    category = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    def create(self, location, product_name, description, image, category, price, stock_quantity):
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
        pass

    def update(self, product_id, **kwargs):
        """Update product details."""
        pass

    def delete(self, product_id):
        """Delete a product."""
        pass

    def calculate_discount(self, discount_percentage):
        """Calculate the discount on the product price."""
        discounted_price = self.price * (1 - discount_percentage / 100)
        return discounted_price

    def process_payment(self, payment_details):
        """Process the payment for the product."""
        pass
