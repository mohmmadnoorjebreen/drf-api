from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Sport(models.Model):
    title = models.CharField(max_length=255)
    sport = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

