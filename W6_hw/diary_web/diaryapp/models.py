from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class diary(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): # 메소드를 overriding : class를 만들 때 기본적으로 주어진다
        # 어디선가 이 객체가 호출이 되었을 때 나오는 이름표 같은 것
        # admin/ page에 Blog Object라고만 나와서 제목을 바꾸려는 것 
        return self.title
    
    def summary(self): # 글이 너무 길 때 요약을 해 주는 method
        return self.body[:100] # 본문이 너무 긴 경우 100자만 잘라서 보여줌