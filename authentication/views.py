from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from django.shortcuts import render, redirect
from .models import UserManage
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_technician:
                return redirect('/technician/dashboard')
            else:
                return redirect('/staff/dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'register.html')

def register_technician(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserManage.objects.create_user(username=username, password=password)
        user.is_technician = True
        user.save()
        messages.success(request, 'Registration successful!')
        context = {'username': username}
        return redirect('/login')
    return render(request, 'register_technician.html')

def register_staff(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserManage.objects.create_user(username=username, password=password)
        user.is_staff_member = True
        user.save()
        messages.success(request, 'Registration successful!')
        context = {'username': username}
        return redirect('/login')
    return render(request, 'register_staff.html')