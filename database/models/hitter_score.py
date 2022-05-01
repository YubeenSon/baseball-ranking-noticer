from database import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String


class HitterScore(Base):
    __tablename__ = 'hitter_score'

    score_id = Column(String(50), primary_key=True)
    
    date = Column(Date(), nullable=False)
    date_int = Column(Integer(), nullable=False)

    # 경기, 타석, 타수
    game_count = Column(Integer())
    plate_appearance = Column(Integer())
    time_at_bat = Column(Integer())

    # 안타, 2루타, 3루타, 홈런
    hit = Column(Integer())
    double = Column(Integer())
    triple = Column(Integer())
    homerun = Column(Integer())

    # 타점, 득점
    runs_batted_in = Column(Integer())
    runs = Column(Integer())

    # 도루, 사사구, 삼진
    stolen_base = Column(Integer())
    base_on_ball = Column(Integer())
    strikeouot = Column(Integer())

    # 타율, 출루율, 장타율, ops
    batting_average = Column(Float())
    on_base_percent = Column(Float())
    sluggin_percentage = Column(Float())
    ops = Column(Float())

    # Foreign Key
    fk_player_id = Column(String(50), ForeignKey("player.player_id"))