import os
from sqlalchemy import create_engine
from .models import Base

# Always use the db file inside lib/db
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "gym.db")
engine = create_engine(f"sqlite:///{DB_PATH}")

def create_database():
    Base.metadata.create_all(engine)
    print(f"SQLite database created at {DB_PATH} with all tables.")

if __name__ == "__main__":
    create_database()