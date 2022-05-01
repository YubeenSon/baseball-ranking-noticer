from database import Base
from sqlalchemy import Column, Date, Float, Integer, String, ForeignKey


class PitcherScore(Base):
    __tablename__ = 'pitcher_score'

    score_id = Column(String(50), primary_key=True)
    
    date = Column(Date(), nullable=False)
    date_int = Column(Integer(), nullable=False)

    # 경기, 승, 패, 세이브, 홀드
    game_count = Column(Integer())
    win = Column(Integer())
    loss = Column(Integer())
    save = Column(Integer())
    hold = Column(Integer())

    # 이닝(자연수부분), 이닝(분수부분), 투구수
    innings_pitched_natural = Column(Integer())
    innings_pitched_fraction = Column(String())
    number_of_pitches = Column(Integer())

    # 피안타, 피홈런
    hit = Column(Integer())
    homerun = Column(Integer())

    # 탈삼진, 사사구, 실점
    strike_out = Column(Integer())
    base_on_balls = Column(Integer())
    run = Column(Integer())

    # 자책, 평균자책, whip
    earned_run = Column(Integer())
    era = Column(Float())
    whip = Column(Float())

    # qs
    quality_start = Column(Integer())

    # Foreign Key
    fk_player_id = Column(String(50), ForeignKey("player.player_id"))
