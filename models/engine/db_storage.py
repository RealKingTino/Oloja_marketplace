#!/usr/bin/python3
""" a module that stores in the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import Base, BaseModel
from models.user import User
from models.product import Product
from models.cart import Cart
from models.marketer import Marketer
from models.order import Order
from models.state import State
from models.category import Category
from models.review import Review
from os import environ
from sys import modules


class DBStorage:
    """
        DBStorage class that implements the storage in database
        Attrs:
            __engine: a private attribute
            __session: a private attribue
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the DBStorage instance. """
        user = environ.get('HBNB_MYSQL_USER')
        passwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            "oloja_dev", "oloja_dev_pwd", "localhost", "oloja_dev_db"), pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Query all object in the current database session.
            Args:
                cls (class): The class to query. If None, query all types of
                objects.
            Returns:
                dict: A dictionary with keys in the format below
                <class-name>.<object-id>
        """
        classes = {
                'User': User, 'Product': Product,
                'State': State, 'Cart': Cart, 'Category': Category,
                'Review': Review, 'Maketer': Marketer, 'Order': Order
                 }
        obj_dict = {}
        for clss in classes:
            if cls is None or cls is clss or cls is classes[clss]:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Add the object to the current database session.
        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session if it's
        not None.

        Args:
            obj (BaseModel): The object to delete from the session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create the current database
        session.
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """close sessions"""
        self.__session.remove()

    def get(self, cls, id):
        """get an object og cls instance with id"""
        objs = self.all(cls)
        key = cls.__name__ + "." + str(id)
        return objs.get(key)

    def count(self, cls=None):
        """count objects of <cls> type"""
        count = 0
        objs = self.all(cls)
        for obj in objs:
            count += 1
        return (count)
