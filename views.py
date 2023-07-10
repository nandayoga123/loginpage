from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # User authentication successful, redirect to dashboard or desired page
            return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')








