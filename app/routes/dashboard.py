# Import Flask and needed modules
from flask import Blueprint, render_template

# Set up dashboard routes
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Get main dashboard page.
@bp.route('/')
def dash():
  return render_template('dashboard.html')

# Get single post to edit.
@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')