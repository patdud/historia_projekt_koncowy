from viewer.models import Level, Category, Article, Question, AnswerType, Answer, Quiz, Quiz_question, User_category

import random

import time

def quiz_generator(request, user, category, level):

    for question in Quiz_question.objects.all():
        print(f"{question.quiz_id.id=} test")

        new_quiz = Quiz(user_id=request.user, name=str(time.time()))
        new_quiz.save()
        quiz_id = new_quiz.id

        selected_questions_by_category = []
        for question in Question.objects.all():
            if str(question.category_id.id) == category and str(question.level_id.id) == level:
                selected_questions_by_category.append(question)

        prepared_quiz = 0
        for question_x in selected_questions_by_category:
            if len(prepared_quiz) < 5:
                chosen_question = random.choice(prepared_quiz)
                new_question = Quiz_question(quiz_id=new_quiz, question_id=chosen_question)
                new_question.save()
                prepared_quiz += 1

    return str(quiz_id)