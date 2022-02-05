from account import views as accountView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('signup/', accountView.SignUp.as_view()),
]
