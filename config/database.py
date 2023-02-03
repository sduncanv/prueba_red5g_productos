from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Product

class Database():
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///database.db')
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()

Base.metadata.create_all(Database().engine)