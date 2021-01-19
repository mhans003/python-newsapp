# Blueprint consolidates routes into a single bp object (parent app can register - similar to Express's Router)
# render_template allows us to send back a template instead of a string.
from flask import Blueprint, render_template
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
  # Render homepage with the retrieved posts.
  return render_template(
    'homepage.html',
    posts=posts
  )

# Get login page
@bp.route('/login')
def login():
  return render_template('login.html')

# Get single post.
@bp.route('/post/<id>')
def single(id):
  # Get single post by id.
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # Render single post template, and pass in retrieved post.
  return render_template(
    'single-post.html',
    post=post
  )