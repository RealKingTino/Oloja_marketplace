#!/usr/bin/python3
""" This is the base module which contain inherited by all other major class
    the project
"""

from datetime import datetime
from uuid import uuid4
import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime


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
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            self.__recreate_method(**kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints the representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the updated_at instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """a method that convert to dictionary

            Return:
                the dictionary representation of an object
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict

    def destroy(self):
        """This method deletes an instance of a User class"""

        name = self.__class__.__name__
        key = name + "." + self.id
        my_dict = models.storage.all()
        if key in my_dict:
            del my_dict[key]
            models.storage.save()




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
