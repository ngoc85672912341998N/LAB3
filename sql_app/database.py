from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL ="sqlite:///./databa1se.db"
SQLALCHEMY_DATABASE_URL = "postgresql://default:lL4DKyesrYj0@ep-rough-sunset-20905830.us-east-1.postgres.vercel-storage.com:5432/verceldb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

