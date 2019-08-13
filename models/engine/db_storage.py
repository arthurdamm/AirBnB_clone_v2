#!/usr/bin/python3
"""Module for DBstorage class"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        from models.base_model import Base
        
        s = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB"))
        print(s)
        print("FOO!")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        # TODO: or before create_all?
        if getenv("HBNB_ENV") == "test":
            metadata.drop_all()

    def all(self, cls=None):
        """returns all objects of cls"""
        from models.state import State
        from models.city import City

        class_list = [
            State,
            City
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """add object to db"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the db"""
        from models.state import State
        from modesl.city import City

        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
