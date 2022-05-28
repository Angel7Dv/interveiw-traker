from django.shortcuts import render, redirect 
from django.contrib.auth import login
from .forms import CreateUserForm       

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, 'index.html')

def register_user(request):		
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            user = form.save()          
            login(request, user)    
            return redirect('index')
    else:
        form = CreateUserForm()
    ctx = {'form':form}

    return render(request, 'register.html', ctx)



@login_required
def user_panel(request):
    return render(request, 'user_panel.html')

