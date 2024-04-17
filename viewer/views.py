from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

import random

from django.urls import reverse_lazy, reverse

from viewer.models import Level, Category, Article, Question, AnswerType, Answer, Quiz, Quiz_question, User_category


# from viewer.forms import SignUpForm


class MainSiteView(View):
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
            return redirect(reverse('quiz', args=[category, '1']))
        elif request.POST.get('novice') is not None:
            return redirect(reverse('quiz', args=[category, '2']))
        elif request.POST.get('intermediate') is not None:
            return redirect(reverse('quiz', args=[category, '3']))
        elif request.POST.get('advanced') is not None:
            return redirect(reverse('quiz', args=[category, '4']))
        elif request.POST.get('master') is not None:
            return redirect(reverse('quiz', args=[category, '5']))
        else:
            return redirect(reverse('index'))


class QuizView(View):
    def get(self, request, **kwargs):
        category = kwargs.get('category', None)
        level = kwargs.get('level', None)


        selected_questions = []
        for question in Question.objects.all():

            if str(question.category_id.id) == category:
                selected_questions.append(question)

        chosen_question = random.choice(selected_questions)

        answers = []
        for answer in Answer.objects.all():

            if answer.question_id.id == chosen_question.id:
                answers.append(answer.content)

        if category is not None and level is not None:
            return render(request, template_name='quiz.html',
                          context={'question': chosen_question.contents, 'answer_1':answers[0], 'answer_2':answers[1], 'answer_3':answers[2], 'answer_4':answers[3]})
