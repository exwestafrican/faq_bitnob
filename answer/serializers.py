from answer.models import Answer
from answer.dynamic_serializers import DynamicFieldsModelSerializer

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from questions.models import Question


class AnswerSerializer(DynamicFieldsModelSerializer):
    replied_by = serializers.SerializerMethodField()
    question_content = serializers.SerializerMethodField()
    replied_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            "question",
            "question_content",
            "answer",
            "url",
            "updated_on",
            "replied_on",
            "replied_by",
        ]
        validators = [
            # no point having the same answer for a question
            UniqueTogetherValidator(
                queryset=Answer.objects.all(),
                fields=["question", "answer"],
                message="You already gave than answer",
            )
        ]

    def get_replied_by(self, obj):
        return obj.replied_by()

    def get_question_content(self, obj):
        return str(obj.question.question_content())

    def get_replied_on(self, obj):
        # returns date created in a specif formatt
        return obj.created.strftime("%b-%d-%Y")

    def get_updated_on(self, obj):
        replied_on = (
            None
            if self.get_replied_on(obj) == obj.updated.strftime("%b-%d-%Y")
            else obj.updated.strftime("%b-%d-%Y")
        )
        return replied_on
