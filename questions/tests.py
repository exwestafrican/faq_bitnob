from django.test import TestCase

# Create your tests here.
from questions.models import Question

Question.objects.active()
Question.objects.create(question="What does a preimum plan offer", category="enquiry")
