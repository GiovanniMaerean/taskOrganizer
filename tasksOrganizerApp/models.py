from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    year = models.IntegerField()
    beginningDate = models.DateField()
    endingDate = models.DateField()

    def __str__(self):
        return f"{self.title} {self.year}"


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=50)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    deadline = models.DateField()
    hour = models.TimeField(default='00:00')
    description = models.TextField(null=True, blank=True)
    PRIORITY_CHOICES = [
        ('3', 'Low'),
        ('2', "Medium"),
        ('1', "High")
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='2')

    def __str__(self):
        return self.name

class UserTO(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
