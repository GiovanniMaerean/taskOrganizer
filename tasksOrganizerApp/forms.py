from django import forms
from .models import Course, Subject, Task


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'place', 'year', 'beginningDate', 'endingDate']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['course', 'name', 'teacher', 'credits']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['subject', 'name', 'deadline', 'hour', 'description', 'priority']
