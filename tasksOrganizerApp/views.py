from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from tasksOrganizerApp.forms import CourseForm


# Create your views here.
def createCourse(request):
    context = {
        'form' : CourseForm(request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createCourse.html', context)

def homePage(request):
    return render(request, 'homePage.html')