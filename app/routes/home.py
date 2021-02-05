# Blueprint consolidates routes into a single bp object (parent app can register - similar to Express's Router)
# render_template allows us to send back a template instead of a string.
from flask import Flask, Blueprint, current_app, request, jsonify, render_template, session, redirect
# Import models
from app.models import Post, User
from app.db import get_db
from flask_mail import Message, Mail
from os import getenv
# Show error messages.
import sys

bp = Blueprint('home', __name__, url_prefix='/')

# Get homepage
@bp.route('/')
def index():
  # Get all stored posts (Query on the connection object, and save result in posts).
  db = get_db()
  posts = (
    db
      .query(Post)
      .order_by(Post.created_at.desc())
      .all()
  )
  # Render homepage with the retrieved posts, as well as whether user is logged in or not.
  return render_template(
    'homepage.html',
    posts=posts,
    loggedIn=session.get('loggedIn')
  )

# Get login page
@bp.route('/login')
def login():
  # If a user isn't yet logged in, render login page.
  if session.get('loggedIn') is None:
    return render_template('login.html')
  # Otherwise, redirect to user dashboard.
  return redirect('/dashboard')

# Get forgot password page
@bp.route('/forgot')
def forgot():
  # If a user is logged in, redirect to dashboard.
  if session.get('loggedIn') is not None:
    return redirect('/dashboard')
  # Otherwise, redirect to forgot password page.
  return render_template('forgot.html')

@bp.route('/forgot', methods=['POST'])
def forgotPasswordEmail():
    print('in forgot route')
    # Capture the request data sent from client, and get session for DB communication.
    data = request.get_json()
    db = get_db()

    # See if this user email exists. Otherwise, send back a 400 error.
    try: 
        user = db.query(User).filter(User.email == data['email']).one()
    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect Credentials'), 400

    # Configure flask mail.
    current_app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    current_app.config['MAIL_PORT'] = 465
    current_app.config['MAIL_USE_SSL'] = True
    current_app.config['MAIL_USERNAME'] = getenv('EMAIL_ADDRESS')
    current_app.config['MAIL_PASSWORD'] = getenv('EMAIL_PASSWORD')

    # Use the current app instance to create instance of Mail object.
    mail= Mail(current_app)

    # Configure email message. 
    msg = Message()
    msg.subject = "Password Reset Link - Python News App"
    msg.recipients = [data['email']]
    msg.sender = getenv('EMAIL_ADDRESS')
    msg.body = 'You have requested to reset your password.'
    mail.send(msg)

    return jsonify(email = user.email)

# Get single post.
@bp.route('/post/<id>')
def single(id):
  # Get single post by id.
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # Render single post template, and pass in retrieved post and whether user is logged in or not.
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )