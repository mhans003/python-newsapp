from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
# Show error messages.
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  # Capture the request data sent from client, and get session for DB communication.
  data = request.get_json()
  db = get_db()

  try:
      # Attempt to create new user.
      # Use data (Python dictionary datatype) to create an object.
      newUser = User(
          username = data['username'],
          email = data['email'],
          password = data['password']
      )

      print(newUser)

      # Save to database.
      db.add(newUser)
      db.commit()
  except:
      print(sys.exc_info()[0])
      # If the insertion failed, rollback the last db commit to prevent server crashing when deployed.
      db.rollback()
      # Send error message back along with server error code.
      return jsonify(message = 'Something went wrong. Refresh and try again.'), 500
  
  # Clear any existing session and add two properties to global session object for session persistence.
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  # Send back the ID of the newly created user.
  return jsonify(id = newUser.id)