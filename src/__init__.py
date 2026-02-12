import os
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

#db = SQLAlchemy(app)

@app.route("/")

def main():
    print("Hello from backend!")
    return "Hello from backend =)"

if __name__ == "__main__":
    main()