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

from django.contrib.auth.models import Permission

from viewer.models import Level, Category, Article, Question, AnswerType, Answer, Quiz, Quiz_question, User_category
from viewer.views import MainSiteView, LevelPrehistoryView, LevelAntiquityView, LevelMedievalView, LevelModernityView, LevelXXAgeView, LevelContemporaryView #, QuizView

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
    path('magivita/', MainSiteView.as_view(), name='index'),
    path('', MainSiteView.as_view(), name='index'),
    path('magivita/prehistory/', LevelPrehistoryView.as_view(), name='prehistory'),
    path('magivita/antiquity/', LevelAntiquityView.as_view(), name='antiquity'),
    path('magivita/medieval/', LevelMedievalView.as_view(), name='medieval'),
    path('magivita/modernity/', LevelModernityView.as_view(), name='modernity'),
    path('magivita/xxage/', LevelXXAgeView.as_view(), name='xxage'),
    path('magivita/contemporary/', LevelContemporaryView.as_view(), name='contemporary'),
    # path('magivita/<category>/<quiz_id>/', QuizView(), name='quiz'),
]
