from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from questions.models import Question

from answer.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(
        trim_whitespace=True,
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=Question.objects.all(),
                message="Hmm, seems this question was already asked, would you like to rephrase? or make a search if you have a similar problem",
            )
        ],
    )
    answer = AnswerSerializer(
        many=True, fields=["answer", "replied_by"], read_only=True
    )
    question_url = serializers.SerializerMethodField()
    date_asked = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "question",
            "category",
            "status",
            "answer",
            "asked_by",
            "date_asked",
            "question_url",
        ]

        read_only_fields = ["answer"]

    def get_question_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.get_absolute_url())

    def get_date_asked(self, obj):
        return obj.date_asked().strftime("%b-%d-%Y")
