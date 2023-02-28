from django.db import models

# Create your models here.


class RandomList(models.Model):
    text = models.TextField()