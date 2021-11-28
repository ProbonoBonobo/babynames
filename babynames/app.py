from flask import Flask
from babynames.database import db, app



@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
