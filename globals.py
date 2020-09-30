
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_config = {
    'host': '127.0.0.1',
    'port': 5432,
    'dbname': 'first_app',
    'user': 'first_user',
    'pass': 'first_pass'
}

engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["pass"]}@'
                       f'{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}',
                       echo=False)

Session = sessionmaker(bind=engine, autoflush=False)

