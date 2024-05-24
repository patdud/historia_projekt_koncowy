from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.core.cache import cache
from django.urls import reverse_lazy, reverse

from viewer.quiz_generator import quiz_generator
from viewer.models import Question, Answer, Quiz, Quiz_question, User_category
from viewer.forms import SignUpForm

import random


class MainSiteView(View):
    def get(self, request):
        return render(
            request, template_name='index.html',
            context={}
        )

    def post(self, request):
        if request.POST.get('prehistory') is not None:
            return redirect(reverse('level', args=['1']))
        elif request.POST.get('ancient') is not None:
            return redirect(reverse('level', args=['2']))
        elif request.POST.get('medieval') is not None:
            return redirect(reverse('level', args=['3']))
        elif request.POST.get('modernity') is not None:
            return redirect(reverse('level', args=['4']))
        elif request.POST.get('xixage') is not None:
            return redirect(reverse('level', args=['5']))
        elif request.POST.get('contemporary') is not None:
            return redirect(reverse('level', args=['6']))


class LevelView(LoginRequiredMixin, View):
    category = None

    def __init__(self):
        super().__init__()
        self.category = None

    def get(self, request, **kwargs):
        category = kwargs.get('category', None)

        if category in ['1', '2', '3', '4', '5', '6']:
            return render(request, template_name='levels.html',
                          context={})
        else:
            return redirect(reverse('index'))

    def post(self, request, **kwargs):
        category = kwargs.get('category', None)

        if request.POST.get('beginner') is not None:
            quiz_generator(request, category, 1)
            return redirect(reverse('quiz'))
        elif request.POST.get('novice') is not None:
            quiz_generator(request, category, 2)
            return redirect(reverse('quiz'))
        elif request.POST.get('intermediate') is not None:
            quiz_generator(request, category, 3)
            return redirect(reverse('quiz'))
        elif request.POST.get('advanced') is not None:
            quiz_generator(request, category, 4)
            return redirect(reverse('quiz'))
        elif request.POST.get('master') is not None:
            quiz_generator(request, category, 5)
            return redirect(reverse('quiz'))
        else:
            return redirect(reverse('index'))


class QuizView(View):
    def get(self, request):
        quiz = Quiz.objects.filter(user_id=request.user).values('id')[0]['id']
        step = Quiz.objects.filter(user_id=request.user).values('quiz_step')[0]['quiz_step']

        if step == 5:
            return redirect(reverse('summary'))

        Quiz.objects.filter(user_id=request.user).update(quiz_step=step+1)

        set_of_questions = []
        for quiz_question in Quiz_question.objects.all():
            if quiz_question.quiz_id.id == quiz:
                set_of_questions.append(quiz_question.question_id)

        answers = []
        for answer in Answer.objects.all():
            if answer.question_id.id == set_of_questions[step].id:
                answers.append((answer.content, set_of_questions[step].score * answer.flag))
        random.shuffle(answers)

        return render(request, template_name='quiz.html',
                      context={'jestemSobieZmienna': 'zmienna niezmienna', 'question': set_of_questions[step].contents, 'answer_1': answers[0],
                               'answer_2': answers[1], 'answer_3': answers[2], 'answer_4': answers[3]})

    def post(self, request):
        quiz = Quiz.objects.filter(user_id=request.user).values('id')[0]['id']

        if request.POST.get('answer') is not None:
            self.choice_made = True
            current_score = Quiz.objects.filter(id=quiz).values('quiz_score')[0]['quiz_score']
            gained_points = int(request.POST.get('answer'))
            new_score = current_score + gained_points

            Quiz.objects.filter(id=quiz).update(quiz_score=new_score)

            return redirect(reverse('quiz'))
        else:
            return redirect(reverse('index'))


class SummaryView(View):
    def get(self, request):
        quiz = Quiz.objects.filter(user_id=request.user).values('id')[0]['id']
        session_id = request.session.session_key

        score = Quiz.objects.filter(id=quiz).values('quiz_score')[0]['quiz_score']
        question_id = Quiz_question.objects.filter(quiz_id=quiz).values('question_id')[0]['question_id']
        category_id = Question.objects.filter(id=question_id).values('category_id')[0]['category_id']
        current_score = User_category.objects.filter(user_id=request.user, category_id=category_id).values('points')[0]['points']
        new_points = current_score + score

        if cache.get(f'action_{session_id}{quiz}') is None:
            cache.set(f'action_{session_id}{quiz}', True, timeout=30)
            User_category.objects.filter(user_id=request.user, category_id=category_id).update(points=new_points)

        return render(request, template_name='summary.html', context={'score': score})


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


def to_main_site(request):
    return redirect('index')
