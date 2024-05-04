from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import Settings

setting = Settings()
engine = create_engine(setting.database_url)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
