from django.shortcuts import render, redirect
from .forms import VacantForm
# Create your views here.

def index(request):
    
    if request.user.is_authenticated:
        return redirect("dashboard")

    return render(request, 'index.html')


def dashboard(request):
    add_vacant_form = VacantForm()
    if request.method == 'POST':

        add_vacant_form = VacantForm(request.POST)
        
        print(add_vacant_form.is_valid())

        if add_vacant_form.is_valid():

            add_vacant_form.save()
            
            redirect("dashboard")


    ctx = {'add_vacant_form': add_vacant_form}


    return render(request, 'traker/dashboard.html', ctx)