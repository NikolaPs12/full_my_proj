from ..extensions import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(100), nullable=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_role = db.Column(db.String(50), nullable=False, default='user')
    post = db.relationship('Post', backref='author', lazy=True)
