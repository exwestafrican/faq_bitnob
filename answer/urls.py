from django.urls import path
from answer import views

urlpatterns = [
    path("", views.AnswerList.as_view(), name="answer-list"),
    path("<pk>/", views.AnswerDetail.as_view(), name="answer-detail"),
]
