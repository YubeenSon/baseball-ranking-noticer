from database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class Team(Base):
    __tablename__ = 'team'

    team_id = Column(String(10), primary_key=True)
    team_name = Column(String(20), nullable=False)

    # Back Reference
    players = relationship("Player", backref="team")