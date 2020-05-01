from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Music(models.Model):
    author=models.CharField(max_length=100,default="Anonymous")
    name=models.CharField(max_length=200)
    desc=models.TextField()
    added=models.DateTimeField(timezone.now)

    def __str__(self):
        return self.name + " " + str(self.added.date()) + " " + str(self.added.time()) 
