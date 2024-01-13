#!/usr/bin/python3

#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """class representing the states table"""
    __tablename__ = 'cities'

