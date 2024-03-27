from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from tasksOrganizerApp.forms import CourseForm, SubjectForm, TaskForm
from .models import Course


class TasksListView(LoginRequiredMixin,ListView):
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


"""def homePage(request):
    return render(request, 'homePage.html')"""


def signInUp(request):
    return render(request, 'signInUp.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.success(request, ("Username or Password is incorrect"))
    return render(request, 'login.html')
