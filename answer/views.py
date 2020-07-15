from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from answer.models import Answer
from answer.serializers import AnswerSerializer

from questions.permissions import IsOwnerOrReadOnly

# Create your views here.


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    fields = ["question", "question_content", "answer", "url"]

    # anyone authenticated user can answer a question

    def list(self, request, *args, **kwargs):
        """ 
        passes fields as a kwarg to 
        get_serializer to customse data
        """
        queryset = self.filter_queryset(self.get_queryset())
        fields = self.fields
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, fields=fields, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    exclude = ["url"]

    def retrieve(self, request, *args, **kwargs):
        # passed in the exclude kwargs to serializer class
        instance = self.get_object()
        serializer = self.get_serializer(instance, exclude=self.exclude)
        return Response(serializer.data)
