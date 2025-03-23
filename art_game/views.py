from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Answer
from art_game import serializers


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answers to be viewed or edited.
    """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class QuestionWithAnswersViewSet(viewsets.ViewSet):
    """
    API endpoint that allows all questions with answers
    to be viewed.
    """

    def list(self, request):
        questions = Question.objects.prefetch_related('answers').all()
        serializer = serializers.QuestionWithAnswersSerializer(
            questions,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)