from rest_framework import viewsets

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