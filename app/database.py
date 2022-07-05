from config import pg_user, pg_password, db_name
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user=pg_user, password=pg_password)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = cursor.execute(f'create database {db_name}')

cursor.close()
connection.close()
