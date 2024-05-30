import os

class Config:
    # Change these to your PostgreSQL database credentials
    POSTGRES_USER = 'your_username'
    POSTGRES_PASSWORD = 'your_password'
    POSTGRES_DB = 'your_database_name'
    POSTGRES_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)