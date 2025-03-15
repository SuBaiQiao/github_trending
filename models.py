from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TrendingRepo(Base):
    __tablename__ = 'trending_repos'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    author = Column(String(100), nullable=False)
    language = Column(String(50))
    stars = Column(String(20))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False),
    type = Column(String(20), nullable=False, comment='daily, weekly, monthly')


# Database connection string
DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/github_trending'

# Create engine and tables
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
