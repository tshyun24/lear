from flask import Flask
from flask_migrate import Migrate

from business_model import db

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

migrate = Migrate(app,
                  db,
                  directory="src/migrations",
                  **{'dialect_name': 'postgres'})