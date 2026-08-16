from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=True,   
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()