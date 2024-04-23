from viewer.models import Level, Category, Article, Question, AnswerType, Answer, Quiz, Quiz_question, User_category

import random

import time

def quiz_generator(request, category, level):

    new_quiz = Quiz(user_id=request.user, name=str(time.time()))
    new_quiz.save()
    quiz_id = new_quiz.id

    selected_questions_by_category = []
    for question in Question.objects.all():
        print("Przed warunkiem")
        if str(question.category_id.id) == category:
            print("Warunek spełniony")
            selected_questions_by_category.append(question)

    prepared_quiz = 0
    while prepared_quiz < 5:
        chosen_question = random.choice(selected_questions_by_category)
        new_question = Quiz_question(quiz_id=new_quiz, question_id=chosen_question)
        new_question.save()
        prepared_quiz += 1

    return str(quiz_id)