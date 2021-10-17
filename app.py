from flask import Flask, flash, redirect, render_template, request, session, Blueprint, Response, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from dotenv import load_dotenv
import mysql.connector
import jwt
from datetime import datetime

app = Flask(__name__)

#loading sensitive information from dotenv file
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# Configuring MYSQl
mydb = mysql.connector.connect(
  host="localhost",
  user=MYSQL_USER,
  password=MYSQL_PASSWORD,
   database=MYSQL_DB
)

# JWT token for the authentication of the user
def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[1]
    return token


mycursor = mydb.cursor()

#function to add admin login details to database
def add_admin():
    sql = "INSERT INTO admin (username, password_hash) VALUES (%s,%s)"
    username="DevinChugh"
    password="devin_206"
    val = (username, generate_password_hash(password))
    mycursor.execute(sql,val)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/",methods=["GET", "POST"])
def insert_tip():
    if request.method == "POST":
        tip=request.form.get("tip")

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO tips (time, tip) VALUES (%s,%s)"
        val = (formatted_date, tip)
        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        flash("Thanks for the Tip!")
        return redirect("/")


@app.route("/admin",methods=["GET", "POST"])
def admin_login():      
    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        mycursor.execute('SELECT * FROM admin WHERE username = %s', (username,))
        # Fetch one record and return result
        account = mycursor.fetchone()

        if len(account) != 1 or not check_password_hash(account[0]["password_hash"],password):
            return flash("invalid username and/or password")
        else:
            user_id=account[0]["id"]
            jwt_token = generate_jwt_token({"id": user_id})
            return jwt_token

    return redirect("/admin")            

