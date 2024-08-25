from app.model import db, Question
import random

def get_all_questions():
    """
    Récupère toutes les questions disponibles dans la base de données.
    """
    return Question.query.all()

def get_question_by_id(question_id):
    """
    Récupère une question par son ID.
    """
    return Question.query.get(question_id)

def get_next_question(current_index, question_ids):
    """
    Récupère la prochaine question en fonction de l'index actuel et de la liste des IDs des questions.
    """
    if current_index < len(question_ids):
        next_question_id = question_ids[current_index]
        return get_question_by_id(next_question_id)
    return None

def check_answer(question_id, user_answer):
    question = get_question_by_id(question_id)
    if not question:
        return False
    
    # S'assurer que user_answer est une chaîne valide
    valid_answers = ['A', 'B', 'C', 'D']
    if user_answer not in valid_answers:
        return False
    
    return question.correct_answer == user_answer

def get_score(answers):
    score = 0
    for answer in answers:
        if len(answer) >= 2:  # S'assurer qu'il y a au moins 2 éléments dans le tuple
            question_id, user_answer = answer[:2]
            if check_answer(question_id, user_answer):
                score += 1
    return score




def get_random_questions(limit=10):
    """
    Récupère un certain nombre de questions aléatoires de la base de données.
    
    Arguments:
    - limit: Nombre de questions à récupérer (par défaut 10).
    
    Retourne:
    - Une liste d'objets Question.
    """
    return Question.query.order_by(db.func.random()).limit(limit).all()