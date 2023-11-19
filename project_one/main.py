from sqlalchemy import create_engine
from urllib.parse import quote

from sqlalchemy.orm import sessionmaker

username = 'NSS'
password = 'S@s!12345'
host = 'localhost'
database_name = 'alchemy'

# URL encode the password
encoded_password = quote(password, safe='')

# Construct the database URL
DATABASE_URL = f'postgresql+psycopg2://{username}:{encoded_password}@{host}/{database_name}'

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)
