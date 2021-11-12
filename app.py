from flask import Flask, request, redirect, render_template
from flask.helpers import flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import tips, Admin, db
from helpers import encrypt_tip,decrypt_tip,checkdata
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv   #for python-dotenv method
from apscheduler.schedulers.background import BackgroundScheduler
import os
load_dotenv()                   #for python-dotenv method

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    admin = {
        'email': 'admin@admin.org',
        'password': 'admin'
    }
    if admin.email == username and safe_str_cmp(
        admin.password.encode('utf-8'), password.encode('utf-8')):
        return admin


# Initialising the app and environment variables
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
jwt = JWT(app, authenticate, 'Admin')
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
    return { 'res': "Hello World"}

# Route for the user to submit tip to backend
@app.route("/submit_tip/<tip>", methods=["GET"])
def submit_tip(tip):
    if tip:
        add_tip=tips(tip=encrypt_tip(tip))
        db.session.add(add_tip)
        db.session.commit()
        return { 'result' : 'Tip Submission Successful!'}
    else:
        print('error')
        return {'result': 'error'}

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
