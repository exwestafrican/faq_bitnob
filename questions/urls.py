from django.urls import path
from questions import views

urlpatterns = [
    path("", views.QuestionList.as_view(), name="question-list"),
    path("<int:pk>/", views.QuestionDetail.as_view(), name="question-detail"),
]
