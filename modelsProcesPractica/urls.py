"""
URL configuration for modelsProcesPractica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
"""from tasksOrganizerApp.views import createCourse, homePage, createSubject, createTask, TasksListView, signInUp, login, \
    register"""
from tasksOrganizerApp.views import createCourse, createSubject, createTask, TasksListView, signInUp, logIn, \
    register, logOut, homePage

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('createCourse/', createCourse, name='createCourse'),
    path('createSubject/', createSubject, name='createSubject'),
    path('createTask/', createTask, name='createTask'),
    #path('homePage/', TasksListView.as_view(template_name='homePage.html'), name='homePage'),
    path('homePage/', homePage, name='homePage'),
    path('', signInUp, name='signInUp'),
    path('accounts/login/', logIn, name='login'),
    path('register/', register, name='register'),
    path('logOut/', logOut, name='logOut')
]
