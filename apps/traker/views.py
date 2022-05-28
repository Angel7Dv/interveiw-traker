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

# http://127.0.0.1:8000/dashboard/<vacant_slug>


def enterprise(request, slug_enterprise):  # set enterprise detail
    enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    vacants = Vacant.objects.filter(enterprise=enterprise)
    form_enterprise = EnterpriseForm(instance=enterprise)

    if request.method == 'POST':
        form_enterprise = EnterpriseForm(request.POST, instance=enterprise)
        if form_enterprise.is_valid():
            form_enterprise.save()
            return redirect('view_enterprise', slug_enterprise)

    else:
        ctx = {
            'form_enterprise': form_enterprise,
            'enterprise': enterprise,
            'vacants': vacants
        }

        return render(request, 'traker/enterprise_detail.html', ctx)


def vacant(request, slug_enterprise, vacant_slug):

    # GET
    vacant = get_object_or_404(Vacant, slug=vacant_slug)
    vacant_form = VacantForm(instance=vacant)
    interviews = Interview.objects.filter(vacant=vacant)

    # DELETE
    if request.method == 'DELETE':
        vacant.delete()
        return JsonResponse({'success': "delete"}), redirect("index")

    elif request.method == 'POST':
        # PUT
        if 'ADD_ENTERPRISE' in request.POST:
            query = request.POST.get('ADD_ENTERPRISE', '')
            vacant = Vacant.objects.get(slug=vacant_slug)

            enterprise = Enterprise.objects.get_or_create(name=query)
            vacant.enterprise = enterprise[0]
            vacant.save()
            return redirect("index")
        # CREATE
        elif vacant_form.is_valid():
            vacant_form.save()
            return redirect("index")

    elif request.method == 'GET':
        ctx = {
            'vacant': vacant,
            'vacant_form': vacant_form,
            'interviews': interviews
        }
        return render(request, "traker/vacants/vacant_detail.html", ctx)


def interview(request, slug_enterprise, vacant_slug, interview_slug):

    # current_enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)
    current_interview = get_object_or_404(Interview, slug=interview_slug)

    interview_form = InterviewForm(instance=current_interview)
    print("here")
    if request.method == 'POST':
        # CREATE
        if "ADD_INTERVIEW" in request.POST:
            query_day = request.POST.get("ADD_INTERVIEW", "")
            new_interview = Interview.objects.create(vacant=current_vacant, day=query_day)
            new_interview.save()
            print(query_day, vacant)
            # new_interview = Interview.objects.create()
            return redirect("vacant", slug_enterprise, vacant_slug)
        # PUT
        else:
            print("here")
            interview_form = InterviewForm(request.POST, instance=current_interview)
            print("valid1")
            print(interview_form.is_valid())
            if interview_form.is_valid():
                print("valid2")
                interview_form.save()
                return redirect("vacant", slug_enterprise, vacant_slug)
            else:
                return JsonResponse({"error": "valid2 error"})


    ctx = {
        'interview':current_interview,
        'vacant': current_vacant,
        'interview_form': interview_form
    }

    return render(request, "traker/interview_detail.html" , ctx)
