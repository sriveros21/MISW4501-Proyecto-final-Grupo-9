from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

#from .user import Base

loaded = load_dotenv('.env.development')

if os.environ.get("DATABASE_URL") is None:
    userdb = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME_QUERIES"]
    port_db=os.environ["DB_PORT"]
    urldb = 'postgresql://' + userdb + ':' + password + '@' + host+ ':' +port_db + '/' + dbname
else:
    urldb = os.environ.get("DATABASE_URL")

engine = create_engine(urldb)

db_session_queries = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session_queries.query_property()

def init_db_queries():
    Base.metadata.create_all(bind=engine)
    