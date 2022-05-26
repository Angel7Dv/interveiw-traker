import imp
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm
from .models import Vacant, Interview, Enterprise

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.




def dashboard(request):
    vacants = Vacant.objects.all()
    interviews = Interview.objects.all()
    Enterprises = Enterprise.objects.all()
    add_vacant_form = VacantForm()
    interview_form = InterviewForm()
    Enterprise_form = EnterpriseForm()
    if request.method == 'POST':
        if 'VACANTS' in request.POST:
            add_vacant_form = VacantForm(request.POST)
            if add_vacant_form.is_valid():
                add_vacant_form.save()
                redirect("dashboard")

        elif 'novacant' in request.POST:
            print("NO VACANTE")
    ctx = {
        'add_vacant_form': add_vacant_form,
        'interview_form': interview_form,
        'Enterprise_form': Enterprise_form,

        'vacants':vacants,
        'interviews':interviews,
        'Enterprises':Enterprises
        }
    return render(request, 'traker/dashboard.html', ctx)


# url delete-vacant/id/
def delete_vacant(request, vacant_id):
    print(request.method)
    
    vacant = get_object_or_404(Vacant, pk=vacant_id)
    vacant.delete()
    
    return redirect("index")
    
    # return JsonResponse({'success': "delete"})

