from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta


db = SQLAlchemy()

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

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable = False)

    def __repr__(self):
        return f"Admin('{self.id}' ,'{self.username}')"
