from django.db import models


class Question(models.Model):

    image = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.image


class Answer(models.Model):

    answer = models.CharField(
        max_length=500
    )
    is_correct = models.BooleanField()
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    def __str__(self):
        return self.answer