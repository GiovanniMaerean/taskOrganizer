from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView

from tasksOrganizerApp.forms import CourseForm, SubjectForm, TaskForm
from .models import Course


class TasksListView(ListView):
    model = Course
    template_name = 'homePage.html'
    context_object_name = 'courses'


# Create your views here.
def createCourse(request):
    context = {
        'form': CourseForm(request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createCourse.html', context)


def createSubject(request):
    context = {
        'form': SubjectForm(request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createSubject.html', context)

def createTask(request):
    context = {
        'form': TaskForm(request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createTask.html', context)


def homePage(request):
    return render(request, 'homePage.html')
