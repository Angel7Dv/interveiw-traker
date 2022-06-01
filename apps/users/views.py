from django.shortcuts import render, redirect 
from django.contrib.auth import login
from .forms import CreateUserForm       

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return redirect("login")


def register_user(request):		
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            user = form.save()          
            login(request, user)    
            return redirect('dashboard')
    else:
        form = CreateUserForm()
    ctx = {'form':form}

    print(form)

    return render(request, 'users/register.html', ctx)




