#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref


place_amenity = Table("association", Base.metadata,
                      Column("place_id",
                             String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id",
                             String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))
# TODO: 2 primary_keys?? wtf


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False)
    number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
    max_guest = Column(Integer,
                       default=0,
                       nullable=False)
    price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []
    reviews = relationship(
        "Review",
        cascade="all,delete",
        backref=backref("place", cascade="all,delete"),
        passive_deletes=True)
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False,
        backref=backref("place_amenities", cascade="all,delete"))

    @property
    def reviews(self):
        """Return list of review instances for file storage
        matching place_id
        """
        return {k: v for k, v in storage.all().items()
                if v.place_id == self.id}

    @property
    def amenities(self):
        """returns list of amenity ids"""
        return {k: v for k, v in storage.all().items()
                if v.amenity_id == self.id}

    @amenities.setter
    def amenities(self, obj):
        """appends amenity id to amenity_id to amentiy_ids"""
        # TODO duplicate ids?
        if type(obj) is Amenity and obj.id not in amenity_ids:
            amenity_ids.append(obj.id)
