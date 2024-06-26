from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from tasksOrganizerApp.forms import CourseForm, SubjectForm, TaskForm
from .models import Course, Task, Subject


class TasksListView(LoginRequiredMixin,ListView):
    model = Course
    template_name = 'homePage.html'
    context_object_name = 'courses'


# Create your views here.
@login_required(login_url='/')
def createCourse(request):
    context = {
        'form': CourseForm(request.POST)
    }
    if context['form'].is_valid():
        course = context['form'].save(commit=False)
        course.creatorUser = request.user
        course.save()
        return redirect('homePage')
    return render(request, 'createCourse.html', context)


@login_required(login_url='/')
def createSubject(request):
    context = {
        'form': SubjectForm(request.user ,request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createSubject.html', context)


@login_required(login_url='/')
def createTask(request):
    context = {
        'form': TaskForm(request.user ,request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'createTask.html', context)


@login_required(login_url='/')
def homePage(request):
    courses = Course.objects.filter(creatorUser=request.user)
    if not courses.exists():
        context = {
            'courses': []
        }
    else:
        context = {
            'courses': courses
        }
    return render(request, 'homePage.html', context)


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


def logIn(request):
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

def logOut(request):
    logout(request)
    return redirect('signInUp')

@login_required(login_url='/')
def taskdetails(request, taskId):
    context = {
        'task' : get_object_or_404(Task, pk=taskId)
    }
    return render(request, 'taskDetails.html', context)


@login_required(login_url='/')
def subjectdetails(request, subjectId):
    context = {
        'subject' : get_object_or_404(Subject, pk=subjectId)
    }
    return render(request, 'subjectDetails.html', context)


@login_required(login_url='/')
def coursedetails(request, courseId):
    context = {
        'course' : get_object_or_404(Course, pk=courseId)
    }
    return render(request, 'courseDetails.html', context)


@login_required(login_url='/')
def deleteTask(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    if request.method == 'POST':
        task.delete()
        return redirect('homePage')
    else:
        return HttpResponse("Bad Request: Only POST requests are allowed for this view.")

@login_required(login_url='/')
def deleteSubject(request, subjectId):
    subject = get_object_or_404(Subject, pk=subjectId)
    if request.method == 'POST':
        subject.delete()
        return redirect('homePage')
    else:
        return HttpResponse("Bad Request: Only POST requests are allowed for this view.")

@login_required(login_url='/')
def deleteCourse(request, courseId):
    course = get_object_or_404(Course, pk=courseId)
    if request.method == 'POST':
        course.delete()
        return redirect('homePage')
    else:
        return HttpResponse("Bad Request: Only POST requests are allowed for this view.")