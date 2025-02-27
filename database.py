from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "sqlite:///./secrets_db.db"

engine = create_engine(SQLALCHEMY_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():   # Генератор соединения с бд
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()