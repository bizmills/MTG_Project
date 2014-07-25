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

class Card (Base):
	__tablename__= "cards"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable=True)
	spellTypes = Column(String(50), nullable=True)
	sets_id = Column(String, ForeignKey('sets.id'), nullable=True)
	rarity = Column(String(30), nullable=True)
	hashId=Column(String(100), nullable=True)

class Collection(Base):
	__tablename__="collections"
	id = Column(Integer, primary_key = True)
	collectionName = Column(String(64), nullable=True)
	users_id= Column(String, ForeignKey('users.id'), nullable = True)

class Collection_item(Base):
	__tablename__="collection_items"
	id = Column(Integer, primary_key = True)
	cards_id = Column(Integer, ForeignKey('cards.id'), nullable = True)
	collections_id = Column(Integer, ForeignKey('collections.id'), nullable = True)
	card = relationship ("Card", backref = "collection_items")
	collection = relationship ("Collection", backref = "collection_items")

class User(Base):
	__tablename__="users"
	id = Column(Integer, primary_key = True)
	userName = Column(String(50), nullable=True)
	email = Column(String(64), nullable=True)
	password = Column(String(64), nullable = True)

class Set(Base):
	__tablename__="sets"
	id = Column(String, primary_key = True)
	setName = Column(String(50), nullable=True)

def main():
    """placeholder"""
    global Base
    global engine
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()