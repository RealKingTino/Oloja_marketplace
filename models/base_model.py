#!/usr/bin/python3
""" This is the base module which contain inherited by all other major class
    the project
"""

from datetime import datetime
from models import declarative_base
from models import Column, Integer, DateTime, String
import uuid


Base = declarative_base()
class BaseModel:
    """BaseModel class serve as a base class for all class
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """class constructor with public instances:
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        if len(kwargs) > 0:
            self.__recreate_method(**kwargs)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints the representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __recreate_method(self, **kwargs):
        """a private method that recreates an instance with
            dict representation
        """
        for attr, value in kwargs.items():
            if attr == 'updated_at' or attr == 'created_at':
                setattr(self, attr, datetime.fromisoformat(value))
            elif attr == '__class__':
                pass
            else:
                setattr(self, attr, value)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass
        return dictionary
