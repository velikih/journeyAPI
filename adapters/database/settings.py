import os

from pydantic import BaseSettings


user = os.getenv('FSTR_DB_LOGIN', 'Daniil')
password = os.getenv('PASSWORD', '123456')
host = os.getenv('FSTR_DB_HOST', '127.0.0.1')
port = os.getenv('FSTR_DB_PORT', '5432')
database = os.getenv('DATABASE', 'app_db')


class Settings(BaseSettings):
    DB_URL: str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
