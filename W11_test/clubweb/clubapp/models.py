from django.db import models

# Create your models here.
class clubs(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length=100)
    numpeople = models.FloatField()

    def __str__(self):
        return self.title