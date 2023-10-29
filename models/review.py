"""describe a review instance"""
from models.base_model import BaseModel, Base
class Review(BaseModel, Base):
    """defines a Category instance"""
    __tablename__ = "review"
