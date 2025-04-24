from django.db import models

class Question(models.Model):
    question_test = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_test
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'date'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text