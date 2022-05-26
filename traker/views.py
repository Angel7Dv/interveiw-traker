import imp
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm
from .models import Vacant, Interview, Enterprise

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.


def dashboard(request):
    vacants = Vacant.objects.all()
    add_vacant_form = VacantForm()

    if request.method == 'POST':
        if 'VACANTS' in request.POST:
            add_vacant_form = VacantForm(request.POST)
            if add_vacant_form.is_valid():
                add_vacant_form.save()
                return redirect("index")
    ctx = {
        'add_vacant_form': add_vacant_form,
        'vacants': vacants,
    }
    return render(request, 'traker/dashboard.html', ctx)


def add_new_enterprise(request, vacant_id):
    query = request.POST.get('query', '')


    if request.method == 'POST':
        vacant = Vacant.objects.get(pk=vacant_id)
        enterprise = Enterprise.objects.get_or_create(name=query)
        enterprise.save()
        vacant.enterprise = enterprise
        vacant.save()
        return redirect("index")
    else:
        return redirect("index")


# url delete-vacant/id/
def delete_vacant(request, vacant_id):
    print(request.method)
    vacant = get_object_or_404(Vacant, pk=vacant_id)
    vacant.delete()
    return redirect("index")
    # return JsonResponse({'success': "delete"})


def view_enterprise(request, name_enterprise):

    enterprise = get_object_or_404(Enterprise, name=name_enterprise)
    print(enterprise)

    ctx = {
        
    }

    return render(request, 'traker/enterprise.html', ctx)
