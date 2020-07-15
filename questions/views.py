from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from questions.models import Question
from questions.serializers import QuestionSerializer
from questions.permissions import IsOwnerOrReadOnly

from answer.serializers import AnswerSerializer

# Create your views here.


class QuestionList(generics.ListCreateAPIView):

    queryset = Question.objects
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "category",
        "question",
        "answer__answer",
        "user__email",
        "user__first_name",
        "user__last_name",
    ]
    # only authenticated users can ask a question

    def get_queryset(self):
        if self.request.user.is_staff:
            # staff users see all question
            return self.queryset.all()
        return self.queryset.active()

    def perform_create(self, serializer):
        # request.user = user that asked a question
        serializer.save(user=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]
