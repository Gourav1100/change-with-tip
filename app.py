from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from forms import tips
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '6cf7cbc2e952d4ccddc2862d3e646346'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



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
def submit_tip():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
