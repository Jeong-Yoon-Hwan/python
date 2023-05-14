from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine(
    "postgresql://postgres:1234@localhost:5432/postgres"
)
base = declarative_base()
Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


