from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.contrib.auth.hashers import check_password
from tasksOrganizerApp.forms import CourseForm, SubjectForm, TaskForm, SignInForm, SignUpForm
from .models import Course, UserTO


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

def signInUp(request):
    return render(request, 'signInUp.html')

def signIn(request):
    form = SignInForm(request.POST)
    context = {
        'form' : form
    }
    if context['form'].is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        if authenticateUser(email, password):
            return redirect('homePage')
        else:
            form.add_error(None, 'Correo electrónico o contraseña incorrectos.')
    else:
        form = SignInForm()
    return render(request, 'signIn.html', context)

def authenticateUser(email, password):
    try:
        user = UserTO.objects.get(email=email)
    except UserTO.DoesNotExist:
        return False
    if email == user.email and password == user.password:
        return True
    else:
        return False



def signUp(request):
    context = {
        'form': SignUpForm(request.POST)
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('homePage')
    return render(request, 'signUp.html', context)