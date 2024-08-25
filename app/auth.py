from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.model import User

def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter((User.username == username) | (User.email == email)).first()
        if user:
            flash('Nom d\'utilisateur ou email déjà utilisé.', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Inscription réussie. Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('login'))
    
    return render_template('auth/login.html')

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Connexion réussie.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Échec de la connexion. Vérifiez votre nom d\'utilisateur et votre mot de passe.', 'danger')
    
    return render_template('auth/login.html')

@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('index'))