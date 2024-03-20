from django.shortcuts import render

from tasksOrganizerApp.forms import CourseForm


# Create your views here.
def createCourse(request):
    context = {
        'form' : CourseForm(request.POST)
    }
    return render(request, 'createCourse.html', context)

def homePage(request):
    return render(request, 'homePage.html')