from django import forms
from .models import Course, Subject, Task, UserTO


class DateInput(forms.DateInput):
    input_type = 'date'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'place', 'year', 'beginningDate', 'endingDate']
        widgets = {
            'beginningDate': DateInput(),  # Usa DatePickerInput para el campo beginningDate
            'endingDate': DateInput(),  # Usa DatePickerInput para el campo finalDate
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['course', 'name', 'teacher', 'credits']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['subject', 'name', 'deadline', 'hour', 'description', 'priority']

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserTO
        fields = ['name', 'email', 'password']


class SignInForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = UserTO
        fields = ['email', 'password']
