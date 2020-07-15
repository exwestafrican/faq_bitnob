from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import settings
from django.shortcuts import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

QUESTION_STATUS = [
    ("active", "Active"),
    ("in_active", "In Active"),
]

QUESTION_CATEGORY = [
    ("enquiry", "Enquiry"),
    ("trouble_shooting", "Trouble Shooting"),
    ("payment", "Payment"),
]


class QuestionQuerySet(models.query.QuerySet):
    def active(self):
        """returns a queryset of active questions"""
        return self.filter(status="active")


class QuestionManager(models.Manager):
    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Question(models.Model):
    """handels the creation of a new question"""

    question = models.TextField(
        help_text="What would you like to know?",
        unique=True,
        error_messages={
            "unique": _(
                "Hmm, seems this question was already asked, would you like to rephrase?"
            )
        },
    )
    status = models.CharField(max_length=100, choices=QUESTION_STATUS, default="active")
    category = models.CharField(
        max_length=350, choices=QUESTION_CATEGORY, default="enquiry"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = QuestionManager()

    class Meta:
        ordering = ["-created"]  # arrange by recently asked

    def __str__(self):
        """
        displays a string represntation of object truncated to 250 chars long
        """
        return self.question[0:250]

    def question_content(self):
        # returns untruncated version of the word
        return self.question

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.pk})

    def date_asked(self):
        return self.created

    @property
    def asked_by(self):
        return str(self.user.__str__())
