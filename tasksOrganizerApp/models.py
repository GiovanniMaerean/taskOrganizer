from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    year = models.IntegerField()
    beginningDate = models.DateField()
    finalDate = models.DateField()


