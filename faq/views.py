from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    # a single entry point to my API
    return Response(
        {
            "questions": reverse("question-list", request=request, format=format),
            "answers": reverse("answer-list", request=request, format=format),
        }
    )
