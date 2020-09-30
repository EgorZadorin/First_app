
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import db_config

engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["pass"]}@'
                       f'{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}',
                       echo=False)

Session = sessionmaker(bind=engine, autoflush=False)

