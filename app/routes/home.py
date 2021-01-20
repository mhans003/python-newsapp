# Blueprint consolidates routes into a single bp object (parent app can register - similar to Express's Router)
# render_template allows us to send back a template instead of a string.
from flask import Blueprint, render_template, session, redirect
# Import models
from app.models import Post
from app.db import get_db

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