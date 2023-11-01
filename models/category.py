"""describe a category instance"""
from models.base_model import BaseModel, Base
class Category(BaseModel, Base):
    """defines a Category instance"""
    __tablename__ = "category"
