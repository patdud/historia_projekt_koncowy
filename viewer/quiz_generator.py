from viewer.models import Category, Question, Quiz, Quiz_question, User_category
from django.contrib.auth.models import User
import random
import time

def quiz_generator(request, category, level):
    Quiz.objects.filter(user_id=request.user).delete()

    new_quiz = Quiz(user_id=request.user, name=str(time.time()))
    new_quiz.save()
    quiz_id = new_quiz.id

    selected_questions_by_category = []
    for question in Question.objects.all():
        if str(question.category_id.id) == category:
            selected_questions_by_category.append(question)

    prepared_quiz = []
    while len(prepared_quiz) < 5:
        chosen_question = random.choice(selected_questions_by_category)
        if chosen_question not in prepared_quiz:
            new_question = Quiz_question(quiz_id=new_quiz, question_id=chosen_question)
            new_question.save()
            prepared_quiz.append(chosen_question)


def create_user_categorys(given_user):
    nowy_user = User.objects.filter(username=given_user)[0]
    print(nowy_user)

    for category in Category.objects.all():
        new_score_relation = User_category(user_id=nowy_user, category_id=category)
        new_score_relation.save()
