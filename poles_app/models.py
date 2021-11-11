from django.db import models
from django.contrib.auth import get_user_model


class Poll(models.Model):
    active = models.BooleanField()
    title = models.CharField(max_length=256)
    pub_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    class Type:
        CUSTOM_TEXT = 'CUSTOM_TEXT'
        ONECHOICE = 'ONECHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (CUSTOM_TEXT, 'CUSTOM_TEXT'),
            (ONECHOICE, 'ONECHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    type = models.CharField(
        max_length=11, choices=Type.choices, default=Type.CUSTOM_TEXT
    )

    def __str__(self):
        return f'{self.text} for {self.poll}'


class AnswerVariant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'Variant for {self.question}'


class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    variant = models.ForeignKey(AnswerVariant, on_delete=models.CASCADE)

