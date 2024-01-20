from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model): # 테이블
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
        #return f'{self.id}.{self.question_text}'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model): # 테이블
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE는 무결성을 지키기위해 부모에 해당하는 참조값이 지워지면 자식에 해당되는 애들도 지워짐
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text