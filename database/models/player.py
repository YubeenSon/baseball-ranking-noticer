from database.models import Base
from sqlalchemy import Column, String


class Player(Base):
    __tablename__ = 'player'

    player_id = Column(String(50), primary_key=True)
    player_name = Column(String(20), nullable=False)
    position = Column(String(10))
    back_number = Column(String(4))
    hitting_hand = Column(String(4))
    pitching_hand = Column(String(4))

    # Foreign Key
    # team_id = 