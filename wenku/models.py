from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    finished =  models.BooleanField()
    last_update = models.DateField()
    num = models.IntegerField(unique=True)
    introduction = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

