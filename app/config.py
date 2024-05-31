import os

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
