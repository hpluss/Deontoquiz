from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'
    

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)  # Texte de la question
    answer_a = db.Column(db.String(128), nullable=False)  # Réponse A
    answer_b = db.Column(db.String(128), nullable=False)  # Réponse B
    answer_c = db.Column(db.String(128), nullable=False)  # Réponse C
    answer_d = db.Column(db.String(128), nullable=False)  # Réponse D
    correct_answer = db.Column(db.String(1), nullable=False)  # Réponse correcte: 'A', 'B', 'C' ou 'D'

    def __repr__(self):
        return f'<Question {self.id}: {self.text}>'



class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactMessage {self.email}>'