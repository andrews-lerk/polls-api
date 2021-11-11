from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('polls/', views.PollsListView.as_view()),
    path('polls/<int:pk>/', views.PollDetailView.as_view()),
    path('question/<int:pk>/', views.QuestionDetailView.as_view()),
    path('reply/', views.AnswerAddView.as_view()),
    path('answers/<int:user_id>/', views.AnswerView.as_view())
]
