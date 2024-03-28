from django.contrib import admin
#from .models import Course, Subject, Task, UserTO
from .models import Course, Subject, Task

# Register your models here.
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Task)
#admin.site.register(UserTO)