from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

engine = create_engine("sqlite:///mtg.db", echo = True)
db_session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = db_session.query_property

class Cards (Base):
	__tablename__= "cards"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable=True)
	spellType = Column(String(50), nullable=True)
	setName = Column(String(50), nullable=True)
	rarity = Column(String(30), nullable=True)
	imageName = Column(String(255), nullable=True)
	hashID=Column(String(255), nullable=True)

class Collection(Base):
	__tablename__="collection"

	id = Column(Integer, primary_key = True)
	cards_id = Column(Integer, nullable = True)
	user = Column(String(30), nullable = True)

def main():
    """placeholder"""
    pass

if __name__ == "__main__":
    main()