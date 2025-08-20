import os
from sqlalchemy import create_engine, text

db_user = os.getenv('POSTGRES_USER', 'flaskuser')
db_password = os.getenv('POSTGRES_PASSWORD', 'flaskpassword')
db_name = os.getenv('POSTGRES_DB', 'flaskdb')
db_host = os.getenv('POSTGRES_HOST', 'pgbouncer')  # using PgBouncer
db_port = os.getenv('POSTGRES_PORT', '6432')

DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(
    DATABASE_URL,
    pool_size=1,
    max_overflow=0,
    pool_timeout=30,
    pool_recycle=1800,
    isolation_level='AUTOCOMMIT'
)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()"))
        return result.fetchone()[0]

# ---------- User Table CRUD ----------
def create_user(name, email):
    with engine.begin() as conn:
        conn.execute(
            text("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT UNIQUE)")
        )
        result = conn.execute(
            text("INSERT INTO users (name, email) VALUES (:name, :email) RETURNING id, name, email"),
            {"name": name, "email": email}
        )
        return dict(result.fetchone()._mapping)

def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, name, email FROM users"))
        return [dict(row._mapping) for row in result]

def get_user_by_id(user_id, conn=None):
    query = text("SELECT id, name, email FROM users WHERE id = :id")
    if conn:
        result = conn.execute(query, {"id": user_id})
    else:
        with engine.connect() as new_conn:
            result = new_conn.execute(query, {"id": user_id})
    row = result.fetchone()
    return dict(row._mapping) if row else None

def update_user(user_id, name=None, email=None):
    with engine.begin() as conn:
        user = get_user_by_id(user_id, conn)
        if not user:
            return None
        if name:
            conn.execute(text("UPDATE users SET name = :name WHERE id = :id"),
                        {"name": name, "id": user_id})
        if email:
            conn.execute(text("UPDATE users SET email = :email WHERE id = :id"),
                        {"email": email, "id": user_id})
        return get_user_by_id(user_id, conn)

def delete_user(user_id):
    with engine.begin() as conn:
        user = get_user_by_id(user_id, conn)
        if not user:
            return False
        conn.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        return True
