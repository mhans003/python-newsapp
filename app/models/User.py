from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
from os import getenv
# Create web token for resetting password.
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Hash passwords
salt = bcrypt.gensalt()

# Create model for a User.
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  # When called, create a reset token (default 30 minutes before expiring).
  def get_reset_token(self, expires_sec=1800):
    s = Serializer(getenv('SECRET_KEY'), expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')

  # Make static (function will not be expecting 'self' parameter).
  @staticmethod
  def verify_reset_token(token):
    s = Serializer(getenv('SECRET_KEY'))
    try: 
      # Try to get payload(user_id) using token (if not expired).
      user_id = s.loads(token)['user_id']
    except: 
      return None
    # If successful, get the user using the user id returned.
    return User.query.get(user_id)

  @validates('email')
  def validate_email(self, key, email):
    # Validate to make sure email address contains @ character.
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 3

    # Return encrypt version of password.
    return bcrypt.hashpw(password.encode('utf-8'), salt)

  # Check incoming password against decrypted stored password.
  def verify_password(self, password):
      return bcrypt.checkpw(
          password.encode('utf-8'),
          self.password.encode('utf-8')
      )