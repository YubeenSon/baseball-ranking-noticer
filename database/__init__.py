import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(verbose=True)

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))

from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Base를 상속받는 model들 alembic에서 확인하기 위한 import
from database.models import hitter_score, pitcher_score, player, team
