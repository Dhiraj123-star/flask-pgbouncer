import os
from sqlalchemy import create_engine,text

db_user = os.getenv('POSTGRES_USER', 'flaskuser')
db_password = os.getenv('POSTGRES_PASSWORD', 'flaskpassword')
db_name = os.getenv('POSTGRES_DB', 'flaskdb')
db_host = os.getenv('POSTGRES_HOST', 'pgbouncer')
db_port = os.getenv('POSTGRES_PORT', '6432')

DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine =create_engine(
    DATABASE_URL, 
    pool_size =1,
    max_overflow = 0,
    pool_timeout = 30,
    pool_recycle = 1800,
    isolation_level='AUTOCOMMIT'
)   

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()"))
        return result.fetchone()[0]