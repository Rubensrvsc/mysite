from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=255)
    closed=models.BooleanField(default=False)
    pub_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.question_text

    def question_closed(self):
        self.closed=True

class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question')
    choice_text=models.CharField(max_length=255)
    votes=models.IntegerField()

    def __str__(self):
        return self.choice_text

    def add_vote(self):
        self.votes=self.votes+1
    
    def add_question(self,question):
        self.question=question