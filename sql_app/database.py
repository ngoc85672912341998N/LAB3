from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL ="sqlite:///./databa1se.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:vuYcO3HTQTx2xqNPV3Ow@containers-us-west-210.railway.app:6524/railway"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

