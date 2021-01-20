from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
# Show error messages.
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

# Create a new user.
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

# Log an existing user in.
@bp.route('/users/login', methods=['POST'])
def login():
    # Capture user login credentials and current session to communicate with db.
    data = request.get_json()
    db = get_db()

    # See if this user exist. Otherwise, send back a 400 error.
    try: 
        user = db.query(User).filter(User.email == data['email']).one()
    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect Credentials'), 400

    # If this user exists, check password (stored in data dictionary) against stored password of this user.
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect Credentials'), 400

    # If successful, clear the current session and mark this user as logged in via the session object.
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True

    return jsonify(id = user.id)

# Log a user out.
@bp.route('/users/logout', methods=['POST'])
def logout():
    # Remove existing session and send back no content code.
    session.clear()
    return '', 204
