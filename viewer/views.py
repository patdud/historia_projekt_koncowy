from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from viewer.quiz_generator import quiz_generator
import random

from django.urls import reverse_lazy, reverse

from viewer.models import Level, Category, Article, Question, AnswerType, Answer, Quiz, Quiz_question, User_category

from viewer.forms import SignUpForm


class MainSiteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request, template_name='index.html',
            context={}
        )

    def post(self, request):
        if request.POST.get('prehistory') is not None:
            return redirect(reverse('level', args=['1']))
        elif request.POST.get('antiquity') is not None:
            return redirect(reverse('level', args=['2']))
        elif request.POST.get('medieval') is not None:
            return redirect(reverse('level', args=['3']))
        elif request.POST.get('modernity') is not None:
            return redirect(reverse('level', args=['4']))
        elif request.POST.get('xxage') is not None:
            return redirect(reverse('level', args=['5']))
        elif request.POST.get('contemporary') is not None:
            return redirect(reverse('level', args=['6']))


class LevelView(View):
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
            return redirect(reverse('quiz', args=[quiz_generator(request, category, 1), '0']))
        elif request.POST.get('novice') is not None:
            return redirect(reverse('quiz', args=[quiz_generator(request, category, 2), '0']))
        elif request.POST.get('intermediate') is not None:
            return redirect(reverse('quiz', args=[quiz_generator(request, category, 3), '0']))
        elif request.POST.get('advanced') is not None:
            return redirect(reverse('quiz', args=[quiz_generator(request, category, 4), '0']))
        elif request.POST.get('master') is not None:
            return redirect(reverse('quiz', args=[quiz_generator(request, category, 5), '0']))
        else:
            return redirect(reverse('index'))


class QuizView(View):
    def get(self, request, **kwargs):
        quiz = kwargs.get('quiz', None)
        step = int(kwargs.get('step', None))
        print(f"Nasz quiz: {quiz} typu {type(quiz)}")

        if step == 5:
            print("koniec quizu")  # Dodać zliczanie punktów - DZIAŁA!
            return redirect(reverse('summary', args=[quiz]))

        set_of_questions = []
        for quiz_question in Quiz_question.objects.all():
            # print(f"{quiz_question.quiz_id.id=} ,{int(quiz)=}")
            if quiz_question.quiz_id.id == int(quiz):
                set_of_questions.append(quiz_question.question_id)

        question = set_of_questions[step]
        print(f"{question=}")
        answers = []
        for answer in Answer.objects.all():
            print(answer)
            print(f"{answer.question_id.id=}, {set_of_questions[step].id}")
            if answer.question_id.id == set_of_questions[step].id:
                answers.append(answer.content)

        return render(request, template_name='quiz.html',
                      context={'question': set_of_questions[step].contents, 'answer_1': answers[0],
                               'answer_2': answers[1], 'answer_3': answers[2], 'answer_4': answers[3]})

    def post(self, request, **kwargs):
        quiz = kwargs.get('quiz', None)
        step = int(kwargs.get('step', None))

        if request.POST.get('answer_A') is not None:
            return redirect(reverse('quiz', args=[quiz, str(step + 1)]))
        elif request.POST.get('answer_B') is not None:
            return redirect(reverse('quiz', args=[quiz, str(step + 1)]))
        elif request.POST.get('answer_C') is not None:
            return redirect(reverse('quiz', args=[quiz, str(step + 1)]))
        elif request.POST.get('answer_D') is not None:
            return redirect(reverse('quiz', args=[quiz, str(step + 1)]))
        else:
            return redirect(reverse('index'))


class SummaryView(View):
    def get(self, request, **kwargs):
        quiz = int(kwargs.get('quiz', None))

        points = 0
        for quiz_question in Quiz_question.objects.all():
            if quiz_question.quiz_id.id == quiz:
                print(f'{quiz_question.question_id.score=}')
                points += quiz_question.question_id.score

        return render(request, template_name='summary.html', context={'points': points})


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


def to_main_site(request):
    return redirect('index')
