from django import forms
#from .models import Course, Subject, Task, UserTO
from .models import Course, Subject, Task


class DateInput(forms.DateInput):
    input_type = 'date'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'place', 'year', 'beginningDate', 'endingDate']
        widgets = {
            'beginningDate': forms.DateInput(),  # Usa DatePickerInput para el campo beginningDate
            'endingDate': forms.DateInput(),  # Usa DatePickerInput para el campo finalDate
        }

class SubjectForm(forms.ModelForm):
    def __init__(self, user, args, **kwargs):
        super(SubjectForm, self).__init__(args, kwargs)
        self.fields['course'].queryset = Course.objects.filter(creatorUser=user)

    class Meta:
        model = Subject
        fields = ['course', 'name', 'teacher', 'credits']

class TaskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(course__creatorUser=user)

    class Meta:
        model = Task
        fields = ['subject', 'name', 'deadline', 'hour', 'description', 'priority']
