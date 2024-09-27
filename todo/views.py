from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth   
 import views as auth_views 

@login_required 
def index(request):
    # ... (rest of the index view code remains the same)

def login(request):
    # If the user is already authenticated, redirect them to the index page
    if request.user.is_authenticated:
        return redirect('index')

    # Otherwise, use Django's built-in login view
    return auth_views.LoginView.as_view(template_name='todo_app/login.html')(request)