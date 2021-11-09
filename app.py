from flask import Flask, request, redirect
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from forms import tips
from datetime import datetime
from cryptography.fernet import Fernet

# initialising fernet
key = Fernet.generate_key()
fernet = Fernet(key)


app = Flask(__name__)
app.config['SECRET_KEY'] = '6cf7cbc2e952d4ccddc2862d3e646346'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def checkdata(data):
    return True

def encrypt_tip(data):
    return fernet.encrypt(data.encode())

def decrypt_tip(data):
    return fernet.decrypt(data).decode()    

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


class tips(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tip = db.Column(db.Text, nullable=False)
    timeline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"tips('{self.id}', '{self.tip}', '{self.timeline}')"


@app.route("/")
def hello():
    return "Hello World"

@app.route("/submit_tip/<data>", methods=["GET","POST"])
def submit_tip(data):
    if checkdata(data):
        add_tip=tips(tip=encrypt_tip(data))
        db.session.add(add_tip)
        db.session.commit()
        return redirect("/")



if __name__ == '__main__':
      app.run(debug=True)
