from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

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
            return redirect(reverse('level', args=['prehistory']))
        elif request.POST.get('antiquity') is not None:
            return redirect(reverse('level', args=['antiquity']))
        elif request.POST.get('medieval') is not None:
            return redirect(reverse('level', args=['medieval']))
        elif request.POST.get('modernity') is not None:
            return redirect(reverse('level', args=['modernity']))
        elif request.POST.get('xxage') is not None:
            return redirect(reverse('level', args=['xxage']))
        elif request.POST.get('contemporary') is not None:
            return redirect(reverse('level', args=['contemporary']))


class LevelView(View):
    category = None

    def __init__(self):
        super().__init__()
        self.category = None

    def get(self, request, **kwargs):
        self.category = kwargs.get('category', None)

        if self.category in ['prehistory', 'antiquity', 'medieval', 'modernity', 'xxage', 'contemporary']:
            return render(request, template_name='levels.html',
                          context={})
        else:
            return redirect(reverse('index'))

    def post(self, request, **kwargs):
        self.category = kwargs.get('category', None)

        if request.POST.get('beginner') is not None:
            return redirect(reverse('quiz', args=[self.category, 'beginner']))
        elif request.POST.get('novice') is not None:
            return redirect(reverse('quiz', args=[self.category, 'novice']))
        elif request.POST.get('intermediate') is not None:
            return redirect(reverse('quiz', args=[self.category, 'intermediate']))
        elif request.POST.get('advanced') is not None:
            return redirect(reverse('quiz', args=[self.category, 'advanced']))
        elif request.POST.get('master') is not None:
            return redirect(reverse('quiz', args=[self.category, 'master']))
        else:
            return redirect(reverse('index'))


class QuizView(View):
    def get(self, request, **kwargs):
        category = kwargs.get('category', None)
        level = kwargs.get('level', None)

        if category is not None and level is not None:
            return render(request, template_name='quiz.html',
                          context={})
