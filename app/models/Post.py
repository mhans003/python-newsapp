from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

# Use datetime to create created_at and updated_at fields
# Reference post's user via Foreign Key.
# When query is made, return property 'user' populated with user's id and username.
# Create a relationship to comments, and when deleted, cascade down and delete associated comments.
# vote_count will add up this post's votes.
class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  vote_count = column_property(
    select([func.count(Vote.id)]).where(Vote.post_id == id)
  )

  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')