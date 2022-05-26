from django.shortcuts import render, redirect
from .forms import VacantForm
from .models import Vacant
# Create your views here.




def dashboard(request):
    vacants = Vacant.objects.all()
    add_vacant_form = VacantForm()
    if request.method == 'POST':
        add_vacant_form = VacantForm(request.POST)
        print(add_vacant_form.is_valid())
        if add_vacant_form.is_valid():
            add_vacant_form.save()
            redirect("dashboard")
    ctx = {
        'add_vacant_form': add_vacant_form,
        'vacants':vacants
        }
    return render(request, 'traker/dashboard.html', ctx)