import imp
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm
from .models import Vacant, Interview, Enterprise

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

# http://127.0.0.1:8000/dashboard/
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

# url delete-vacant/id/
def vacant(request, vacant_slug):

    if request.method == 'DELETE':
        vacant = get_object_or_404(Vacant, slug=vacant_slug)
        vacant.delete()
        return JsonResponse({'success': "delete"}), redirect("index")
    else:
        print(vacant_slug)
        return render(request, "traker/vacant_detail.html")



# http://127.0.0.1:8000/dashboard/add-new-enterprise/0/
def add_new_enterprise(request, vacant_id):
    query = request.POST.get('query', '')
    if request.method == 'POST':
        vacant = Vacant.objects.get(pk=vacant_id)
        enterprise = Enterprise.objects.get_or_create(name=query)
        vacant.enterprise = enterprise[0]
        vacant.save()
        return redirect("index")


def view_enterprise(request, slug_enterprise):
    enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)

    vacants = Vacant.objects.filter(enterprise=enterprise)

    print(vacants)
    form_enterprise = EnterpriseForm(instance=enterprise)

    ctx = {
        'form_enterprise':form_enterprise,
        'enterprise':enterprise,
        'vacants':vacants
    }

    return render(request, 'traker/enterprise.html', ctx)
