"""
URL configuration for magi_vita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.models import (Level,
                           Category,
                           Article,
                           Question,
                           AnswerType,
                           Answer,
                           Quiz,
                           Quiz_question,
                           User_category)

from viewer.views import (LevelView, MainSiteView, QuizView, SubmittableLoginView, SignUpView, CustomLogoutView,
                          to_main_site, SummaryView)

admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(AnswerType)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Quiz_question)
admin.site.register(User_category)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/register/', SignUpView.as_view(), name='register'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', to_main_site),
    path('magivita/', MainSiteView.as_view(), name='index'),
    path('', to_main_site),
    path('magivita/category/<category>/', LevelView.as_view(), name='level'),
    path('magivita/quiz/', QuizView.as_view(), name='quiz'),
    path('magivita/summary/', SummaryView.as_view(), name='summary')
]
