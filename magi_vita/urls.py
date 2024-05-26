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

from viewer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.SubmittableLoginView.as_view(), name='login'),
    path('accounts/register/', views.SignUpView.as_view(), name='register'),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.to_main_site),
    path('magivita/', views.MainSiteView.as_view(), name='index'),
    path('', views.to_main_site),
    path('magivita/category/<category>/', views.LevelView.as_view(), name='level'),
    path('magivita/quiz/', views.QuizView.as_view(), name='quiz'),
    path('magivita/summary/', views.SummaryView.as_view(), name='summary')
]
