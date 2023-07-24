from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
with engine.connect() as connection:
    connection.execute(text('set search_path to "%s"' % settings.POSTGRES_SCHEMA))
    # connection.commit()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
