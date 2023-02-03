from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False, unique = True)
    val = Column(Integer, nullable = False)
    cant = Column(Integer, nullable = False, default = 0)

    def __str__(self) -> str:
        return self.name