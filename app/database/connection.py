from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import pg_user, pg_password, pg_host, db_name


def connect_to_database():
    engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_all_tables():
    engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{db_name}')
    from app.database.models import Base
    Base.metadata.create_all(engine)
