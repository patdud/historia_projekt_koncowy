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

        category = Category.objects.all()

        return render(
            request, template_name='index.html',
            context={'category': category}
        )

    def post(self, request):
        if request.POST.get('prehistory') is not None:
            return redirect(reverse('prehistory'))
        elif request.POST.get('antiquity') is not None:
            return redirect(reverse('antiquity'))
        elif request.POST.get('medieval') is not None:
            return redirect(reverse('medieval'))
        elif request.POST.get('modernity') is not None:
            return redirect(reverse('modernity'))
        elif request.POST.get('xxage') is not None:
            return redirect(reverse('xxage'))
        elif request.POST.get('contemporary') is not None:
            return redirect(reverse('contemporary'))


class LevelPrehistoryView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )


class LevelAntiquityView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )


class LevelMedievalView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )


class LevelModernityView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )


class LevelXXAgeView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )


class LevelContemporaryView(View):
    def get(self, request):
        return render(
            request, template_name='levels.html',
            context={}
        )