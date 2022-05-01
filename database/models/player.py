from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Player(Base):
    __tablename__ = 'player'

    player_id = Column(String(50), primary_key=True)
    player_name = Column(String(20), nullable=False)
    position = Column(String(10))
    back_number = Column(String(4))
    hitting_hand = Column(String(4))
    pitching_hand = Column(String(4))

    # Foreign Key
    fk_team_id = Column(String(10), ForeignKey("team.team_id"))

    # Back Reference
    hitter_scores = relationship("HitterScore", backref="player_hitter")
    pitcher_scores = relationship("PitcherScore", backref="player_pitcher")