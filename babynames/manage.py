# manage.py

from flask_script import Manager

from babynames.app import app
from babynames.database import db
import pdb
import pandas as pd

manager = Manager(app)

@manager.command
def hello():
    print("hello")
    result = db.engine.execute("select * from NationalNames LIMIT 5;")
    print(result.fetchall())


if __name__ == "__main__":
    manager.run()
