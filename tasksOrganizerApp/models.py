from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    year = models.IntegerField()
    beginningDate = models.DateField()
    finalDate = models.DateField()

    def __str__(self):
        return f"{self.title} {self.year}"


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=50)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


    