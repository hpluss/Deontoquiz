from flask import render_template,session,redirect,url_for,request
from flask import current_app as app
from datetime import datetime
import time

from app.auth import register, login, logout
from app.service import get_random_questions, get_next_question, check_answer, get_score
from .model import db, ContactMessage

@app.route('/')
def index():
    return render_template('index.html')


# Routes d'authentification
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.route('/start_quiz')
def start_quiz():
    questions = get_random_questions(limit=10)
    session['questions'] = [q.id for q in questions]
    session['current_index'] = 0
    session['user_answers'] = []
    session['start_time'] = int(time.time())
    return redirect(url_for('next_question'))

@app.route('/next_question')
def next_question():
    current_index = session.get('current_index', 0)
    question_ids = session.get('questions', [])

    if current_index < len(question_ids):
        question = get_next_question(current_index, question_ids)
        start_time = session.get('start_time', int(time.time()))
        return render_template('question.html', 
                               question=question, 
                               current_index=current_index,
                               total_questions=len(question_ids),
                               start_time=start_time)
    else:
        return redirect(url_for('results'))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_answer = request.form.get('answer', '').upper()  # Convertir en majuscules
    question_id = request.form.get('question_id')
    time_spent = request.form.get('time_spent', '0')
    
    # Récupérer l'ID de la question actuelle à partir de la session
    current_index = session.get('current_index', 0)
    question_ids = session.get('questions', [])
    
    if current_index < len(question_ids):
        question_id = question_ids[current_index]
    else:
        # Gérer le cas où l'index est hors limites
        return redirect(url_for('results'))

    # Conversion de time_spent en entier
    try:
        time_spent = int(time_spent)
    except ValueError:
        time_spent = 0

    # Ajouter la réponse à la session
    session['user_answers'].append((question_id, user_answer, time_spent))
    
    # Incrémenter l'index pour la prochaine question
    session['current_index'] = current_index + 1

    # Log pour le débogage
    print(f"Question ID: {question_id}, User Answer: {user_answer}, Time Spent: {time_spent}")

    return redirect(url_for('next_question'))

@app.route('/results')
def results():
    user_answers = session.get('user_answers', [])
    score = get_score(user_answers)
    total_questions = len(session.get('questions', []))
    questions_answered = len(user_answers)
    
    total_time = int(time.time()) - session.get('start_time', 0)
    minutes, seconds = divmod(total_time, 60)
    time_str = f"{minutes:02d}:{seconds:02d}"

    return render_template('results.html', 
                           score=score, 
                           total_questions=total_questions,
                           questions_answered=questions_answered,
                           time_taken=time_str)


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        
        print('Votre message a été envoyé avec succès!', 'success')
        return redirect(url_for('index'))