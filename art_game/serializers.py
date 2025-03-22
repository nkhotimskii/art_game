from rest_framework import serializers

from art_game import models


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Question
        fields = '__all__'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Answer
        fields = '__all__'