from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

# flask app
m_app = Flask(__name__)
m_app.config.from_object(Config)

# flask db
m_db = SQLAlchemy(m_app)

# flask migrate
m_migrate = Migrate(m_app, m_db)

from muse import models, routes