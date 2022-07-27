from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import pg_user, pg_password, pg_host, db_name


def create_all_tables(eng):
    from app.database.models import Base

    Base.metadata.create_all(eng)


engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{db_name}')
create_all_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
