from flask import Flask
# Include routes.
from app.routes import home, dashboard, api
from app.db import init_db
# Allow us to use template filters (in utils folder).
from app.utils import filters

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  #Define first route. This turns return statement into route's response
  @app.route('/hello')
  def hello():
      return 'Sample'

  # Register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.register_blueprint(api)

  # Call imported init_db function to create tables.
  # Due to configuration in init_db, connections won't remain open.
  init_db(app)

  # Register template filters with Jinja template environment.
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural

  return app