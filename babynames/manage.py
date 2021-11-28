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

@manager.command
def db_shell():
    while True:
        try:
            cmd = input("sql> ")
            if cmd == "exit":
                break
            result = db.engine.execute(cmd)
            print(result.fetchall())
        except Exception as e:
            print(f"{e.__class__.__name__} while executing {cmd} ::  {e}. Check your syntax and make sure your identifiers correctly refer to the columns defined in the table schema.")


if __name__ == "__main__":
    manager.run()
