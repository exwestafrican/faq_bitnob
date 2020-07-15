from django.db import models
from django.contrib.auth import settings
from django.shortcuts import reverse

from questions.models import Question

# Create your models here.

User = settings.AUTH_USER_MODEL


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.CASCADE
    )
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        order_with_respect_to = "question"  # one question --> many answers
        unique_together = ["question", "answer"]

    def __str__(self):
        return self.answer[0:250]

    def answer_content(self):
        return self.answer

    def replied_by(self):
        return str(self.user.__str__())

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk": self.pk})
