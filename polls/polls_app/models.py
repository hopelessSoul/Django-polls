from django.db import models

from users.models import Profile


class Poll(models.Model):
    name = models.CharField(max_length=120, blank=True, null=False)
    start_date = models.DateTimeField(auto_now=True, editable=False)
    end_date = models.DateTimeField(null=True, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200, blank=False, null=False)
    question_type = models.CharField(max_length=120)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='choice')
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
