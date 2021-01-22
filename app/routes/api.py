from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db
# Show error messages.
import sys
# Import decorator function to protect routes.
from app.utils.auth import login_required

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
    # Capture request data and current session to communicate with db.
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

# Post a comment.
@bp.route('/comments', methods=['POST'])
@login_required
def comment():
    # Capture request data and session to communicate with db.
    data = request.get_json()
    db = get_db()

    # Try to create the new comment (using passed in data and current user ID from global session object) and add to the database.
    try:
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
        )

        db.add(newComment)
        db.commit()
    except: 
        print(sys.exc_info()[0])

        # If the insertion failed, rollback the last db commit to prevent server crashing when deployed.
        db.rollback()
        # Send error message back along with server error code.
        return jsonify(message = 'Failed to post comment. Try again.'), 500
    
    # If successful, return the newly created comment id.
    return jsonify(id = newComment.id)

# Upvote a post.
@bp.route('/posts/upvote', methods=['PUT'])
@login_required
def upvote():
    # Capture request data and current session to communicate with db.
    data = request.get_json()
    db = get_db()

    try: 
        # Create new vote object using passed in post id and stored user id.
        newVote = Vote(
            post_id = data['post_id'],
            user_id = session.get('user_id')
        ) 

        db.add(newVote)
        db.commit()
    except: 
        print(sys.exc_info()[0])

        # If the insertion failed, rollback the last db commit to prevent server crashing when deployed.
        db.rollback()
        # Send error message back along with server error code.
        return jsonify(message = 'Failed to upvote. Try again.'), 500
    
    # If successful, return.
    return '', 204

# Create a new post.
@bp.route('/posts', methods=['POST'])
@login_required
def create():
    # Capture request data and current session to communicate with db.
    data = request.get_json()
    db = get_db()

    # Try creating a new post using data sent from client and the session object's user id.
    try: 
        newPost = Post(
            title = data['title'],
            post_url = data['post_url'],
            user_id = session.get('user_id')
        )

        db.add(newPost)
        db.commit()
    except:
        print(sys.exc_info()[0])

        # If the insertion failed, rollback the last db commit to prevent server crashing when deployed.
        db.rollback()
        # Send error message back along with server error code.
        return jsonify(message = 'Failed to create new post. Try again.'), 500

    # If successful, send back the newly created post id.
    return jsonify(id = newPost.id)

# Update an existing post.
@bp.route('/posts/<id>', methods=['PUT'])
@login_required
def update(id):
    # Capture request data and current session to communicate with db.
    data = request.get_json()
    db = get_db()

    try: 
        # Find the matching post using the passed in id.
        post = db.query(Post).filter(Post.id == id).one()
        # Update the retrieved post's title.
        post.title = data['title']
        db.commit()
    except: 
        print(sys.exc_info()[0])

        # If the edit failed, rollback the last db commit to prevent server crashing when deployed.
        db.rollback()
        # Send error message back along with server error code.
        return jsonify(message = 'Failed to update a post.'), 404

    return '', 204

# Delete an existing post.
@bp.route('/posts/<id>', methods=['DELETE'])
@login_required
def delete(id):
    # Capture current session to communicate with db.
    db = get_db()

    try:
        # Delete the post from db by retrieving the correct post by id.
        db.delete(db.query(Post).filter(Post.id == id).one())
        db.commit()
    except:
        print(sys.exc_info()[0])

        # If delete failed, rollback the last db commit to prevent server crashing when deployed.
        db.rollback()
        # Send error message back along with server error code.
        return jsonify(message = 'Failed to delete a post.'), 404

    return '', 204