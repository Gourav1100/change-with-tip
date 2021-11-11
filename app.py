from flask import Flask, request, redirect, render_template
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from models import tips, Admin, db
from helpers import encrypt_tip,decrypt_tip,checkdata
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
import os
from apscheduler.schedulers.background import BackgroundScheduler


# Initialising the app and environment variables
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Scheduling the job to automatically delete the tips after 24 hours
sched = BackgroundScheduler(daemon=True)
sched.add_job(tips.delete_expired_tips,'interval',minutes=1)
sched.start()


@app.route("/")
def hello():
    return "Hello World"

# Route for the user to submit tip to backend
@app.route("/submit_tip/<data>", methods=["GET","POST"])
def submit_tip(data):
    if checkdata(data):
        add_tip=tips(tip=encrypt_tip(data))
        db.session.add(add_tip)
        db.session.commit()
        return "Tip Submission Successful!"


# Route for the Admin to login
@app.route("/login/<username>/<password>", methods=["POST"])
def login_admin(username, password):
    user=Admin.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash ,password):
        flash("Login Successful!")
        return redirect("/admin_home")
    return True

# Admin Home route to show the tips received
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
