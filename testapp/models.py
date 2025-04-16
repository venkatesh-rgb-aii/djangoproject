from django.db import models

# Create your models here.
class Movies(models.Model):
    moviename=models.CharField(max_length=255)
    hero=models.CharField(max_length=255)
    heroine=models.CharField(max_length=255)
    rating=models.IntegerField()
    releaseyear=models.IntegerField()