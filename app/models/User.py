from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

# Hash passwords
salt = bcrypt.gensalt()

# Create model for a User.
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

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