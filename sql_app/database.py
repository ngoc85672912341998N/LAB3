from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL ="sqlite:///./databa1se.db"
SQLALCHEMY_DATABASE_URL = "postgres://ngoc:CpNdfzvhEQCXVmL8RgssqscmohAKbzGe@dpg-cj26rq98g3n1jki0gkj0-a/customer123"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

