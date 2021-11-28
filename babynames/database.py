from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile("config.cfg")

# Create the database object
db = SQLAlchemy(app)