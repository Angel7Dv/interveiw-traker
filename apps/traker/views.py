from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm
from .models import Vacant, Interview, Enterprise

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

# http://127.0.0.1:8000/dashboard/


def dashboard(request):
    vacants = Vacant.objects.all()
    add_vacant_form = VacantForm()
    print(add_vacant_form)
    if request.method == 'POST':
        if 'VACANTS' in request.POST:
            add_vacant_form = VacantForm(request.POST)

            if add_vacant_form.is_valid():
                new_vacant = add_vacant_form.save(commit=False)
                new_vacant.user_register = request.user
                new_vacant.save()
                
                return redirect("index")
            else:
                print("no valid")
    ctx = {
        'add_vacant_form': add_vacant_form,
        'vacants': vacants,
    }
    return render(request, 'dashboard.html', ctx)

# http://127.0.0.1:8000/dashboard/<vacant_slug>


def enterprise(request, slug_enterprise):  # set enterprise detail
    enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    vacants = Vacant.objects.filter(enterprise=enterprise)
    form_enterprise = EnterpriseForm(instance=enterprise)

    if request.method == 'POST':
        form_enterprise = EnterpriseForm(request.POST, instance=enterprise)
        if form_enterprise.is_valid():
            new_enterprise = form_enterprise.save(commit=False)
            new_enterprise.user_register = request.user
            new_enterprise.save()
            return redirect('enterprise', slug_enterprise)

    else:
        ctx = {
            'form_enterprise': form_enterprise,
            'enterprise': enterprise,
            'vacants': vacants
        }

        return render(request, 'view_enterprise.html', ctx)


def vacant(request, slug_enterprise, vacant_slug):
    # GET
    vacant = get_object_or_404(Vacant, slug=vacant_slug)
    vacant_form = VacantForm(instance=vacant)
    interviews = Interview.objects.filter(vacant=vacant)

    print(request.method,)

    # DELETE
    if request.method == 'DELETE':
        vacant.delete()
        return JsonResponse({'success': "delete"}), redirect("index")

    elif request.method == 'POST':
        print("method POST")
        print(vacant_form.is_valid())
        # CREATE ENTERPRISE
        if 'ADD_ENTERPRISE' in request.POST:
            query = request.POST.get('ADD_ENTERPRISE', '')
            vacant = Vacant.objects.get(slug=vacant_slug)
            enterprise = Enterprise.objects.get_or_create(name=query)
            vacant.enterprise = enterprise[0]
            vacant.save()
            return redirect("index")
        # PUT
        else:
            vacant_form = VacantForm(request.POST, instance=vacant)
            if vacant_form.is_valid():
                new_vacant = vacant_form.save(commit=False)
                new_vacant.user_register = request.user
                new_vacant.save()
                vacant_form.save()
                return redirect("vacant", slug_enterprise, vacant_slug)

            else:
                return JsonResponse({"error": "valid2 error"})

    ctx = {
        'vacant': vacant,
        'vacant_form': vacant_form,
        'interviews': interviews
    }
    return render(request, "view_vacant.html", ctx)


def interview(request, slug_enterprise, vacant_slug, interview_slug):

    # current_enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)
    current_interview = get_object_or_404(Interview, slug=interview_slug)

    interview_form = InterviewForm(instance=current_interview)
    if request.method == 'POST':
        # CREATE
        interview_form = InterviewForm(request.POST, instance=current_interview)
        if interview_form.is_valid():
            new_interview = interview_form.save(commit=False)
            new_interview.user_register = request.user
            new_interview.save()
            return redirect("vacant", slug_enterprise, vacant_slug)
        else:
            return JsonResponse({"error": "valid2 error"})


    ctx = {
        'interview':current_interview,
        'vacant': current_vacant,
        'interview_form': interview_form
    }

    return render(request, "view_interview.html" , ctx)

def add_interview(request, vacant_slug):
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)

    if "ADD_INTERVIEW" in request.POST:
        query_day = request.POST.get("ADD_INTERVIEW", "")
        new_interview = Interview.objects.create(vacant=current_vacant, day=query_day)
        new_interview.save()
        return redirect("index")

