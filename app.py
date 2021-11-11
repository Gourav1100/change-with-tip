from flask import Flask, request, redirect, render_template
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
#from forms import tips
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
import os
from apscheduler.schedulers.background import BackgroundScheduler

# initialising fernet
key = os.environ.get("FERNET_KEY")
fernet = Fernet(key)


app = Flask(__name__)
app.config['SECRET_KEY'] = '6cf7cbc2e952d4ccddc2862d3e646346'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

def checkdata(data):
    return True

# Functions to encrypt and decrypt the tips given by user
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


    # Functions to delete the tips after 24 hours
    @classmethod
    def delete_expired(cls):
        expiration_days = 1
        limit = datetime.utcnow() - timedelta(expiration_days)
        cls.query.filter(cls.timeline > limit).delete()
        db.session.commit()


    def delete_expired_tips():
        tips.delete_expired()

# Scheduling the job to automatically delete the tips after 24 hours
sched = BackgroundScheduler(daemon=True)
sched.add_job(tips.delete_expired_tips,'interval',minutes=1)
sched.start()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable = False)

    def __repr__(self):
        return f"Admin('{self.id}' ,'{self.username}')"



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

@app.route("/login/<username>/<password>", methods=["POST"])
def login_admin(username, password):
    user=admin.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash ,password):
        flash("Login Successful!")
        return redirect("/admin_home")
    return redirect("/")

@app.route("/admin_home")
def get_tips():
    tips_rec = tips.query.all()
    data=[]
    for tip in tips_rec:
        dic={}
        dic["id"]=tip.id
        dic["timeline"]=tip.timeline
        dic["tip"]=decrypt_tip(tip.tip)
        data.append(dic)
    return {'data': data }
    # return render_template("admin_home.html", data=data)

if __name__ == '__main__':
      app.run(debug=True)
