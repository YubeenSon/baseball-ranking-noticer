from database.models import Base
from sqlalchemy import Column, String


class Team(Base):
    __tablename__ = 'team'

    team_id = Column(String(10), primary_key=True)
    team_name = Column(String(20), nullable=False)