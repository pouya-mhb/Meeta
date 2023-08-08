from django.shortcuts import render, redirect
from django.http import HttpResponse
from mvp.models import Meeting
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from mvp.forms import LoginForm, RegisterForm

# Create your views here.


def meetings(request):

    if request.method == 'GET':
        meetings = Meeting.objects.all()
        users = User.objects.all()
        context = {
            'users': users,
            'meetings': meetings,
        }

        return render(
            request, 'meetings.html', context
        )

    if request.method == 'POST':
        pass
    else:
        meetings = Meeting.objects.all()
        users = User.objects.all()
        context = {
            users: users,
            meetings: meetings
        }

        return render(
            request, 'meetings.html', context
        )


def new_meeting(request):
    if request.method == 'POST':
        pass
    else:
        pass


def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return redirect('login')
    else:
        userRegisterForm = RegisterForm()
        return render(request, "LogAppFront/Register.html", {"RegisterForm": userRegisterForm, 'title': 'Register'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO,
                                 "نام کاربری یا رمز عبور اشتباه است")
            return redirect('login')
    else:
        LoginForm()
        return render(request, "LogAppFront/login.html", {
            "loginForm": LoginForm
        })


def user_logout(request):
    logout(request)
    return redirect('login')
