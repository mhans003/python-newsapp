# Blueprint consolidates routes into a single bp object (parent app can register - similar to Express's Router)
# render_template allows us to send back a template instead of a string.
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# Get homepage
@bp.route('/')
def index():
  return render_template('homepage.html')

# Get login page
@bp.route('/login')
def login():
  return render_template('login.html')

# Get single post
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')