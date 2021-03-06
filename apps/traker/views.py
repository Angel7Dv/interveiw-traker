from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm, NetWorkingForm
from .models import Vacant, Interview, Enterprise, NetWorking

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

# http://127.0.0.1:8000/dashboard/
def dashboard(request):
    """allow add vacancies"""
    vacants = Vacant.objects.filter(user_added=request.user)
    add_vacant_form = VacantForm()

    if request.method == 'POST':
        if 'VACANTS' in request.POST:
            add_vacant_form = VacantForm(request.POST)
            if add_vacant_form.is_valid():
                new_vacant = add_vacant_form.save(commit=False)
                new_vacant.user_added = request.user
                new_vacant.save()
                return redirect("dashboard")
            else:
                print("no valid")
    ctx = {
        'add_vacant_form': add_vacant_form,
        'vacants': vacants,
    }
    return render(request, 'dashboard/dashboard.html', ctx)


# http://127.0.0.1:8000/dashboard/<vacant_slug>
def vacant(request, vacant_slug):
    """allow get current vacant, enterprise of vacant, networking and interviews"""

    # GET
    vacant = get_object_or_404(Vacant, slug=vacant_slug)
    vacant_form = VacantForm(instance=vacant)

    interviews = Interview.objects.filter(vacant=vacant)
    networking = NetWorking.objects.filter(vacant=vacant)

    # DELETE
    if request.method == 'DELETE':
        """ get this by fetch from http://127.0.0.1:8000/dashboard/ """
        vacant.delete()
        return redirect("dashboard")

    elif request.method == 'POST':
        # CREATE ENTERPRISE
        """ get this by for m with tag"""
        if 'ADD_ENTERPRISE' in request.POST:
            query = request.POST.get('ADD_ENTERPRISE', '')
            vacant = Vacant.objects.get(slug=vacant_slug)
            enterprise = Enterprise.objects.get_or_create(user_added=request.user, name=query)
            vacant.enterprise = enterprise[0]
            vacant.save()
            return redirect("vacant", vacant_slug)
        # PUT Vacant
        else:
            vacant_form = VacantForm(request.POST, instance=vacant)
            if vacant_form.is_valid():
                new_vacant = vacant_form.save(commit=False)
                new_vacant.user_added = request.user
                new_vacant.save()
                vacant_form.save()
                return redirect("vacant", vacant_slug)

            else:
                return JsonResponse({"error": "valid2 error"})
    ctx = {
        'vacant': vacant,
        'vacant_form': vacant_form,
        'interviews': interviews,
        'networking': networking,
    }
    return render(request, "vacant/vacant.html", ctx)


def interview(request, vacant_slug, pk):
    # current_enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)
    current_interview = get_object_or_404(Interview, pk=pk)
    interview_form = InterviewForm(instance=current_interview)
    if request.method == 'POST':
        # PUT
        interview_form = InterviewForm(
            request.POST, instance=current_interview)
        if interview_form.is_valid():
            new_interview = interview_form.save(commit=False)
            new_interview.user_added = request.user
            new_interview.save()
            return redirect("interview", vacant_slug, pk)
        else:
            return JsonResponse({"error": "valid2 error"})
    ctx = {
        'interview': current_interview,
        'vacant': current_vacant,
        'interview_form': interview_form
    }

    return render(request, "interview.html", ctx)


def post_interview(request, vacant_slug):

    if "ADD_INTERVIEW" in request.POST:
        current_vacant = get_object_or_404(Vacant, slug=vacant_slug)
        query_day = request.POST.get("ADD_INTERVIEW", "")

        new_interview = Interview.objects.create(
            vacant=current_vacant, day=query_day)
        new_interview.save()
        return redirect("vacant", current_vacant.slug)

    if "DELETE_INTERVIEW" in request.POST:
        interview_slug = vacant_slug
        current_interview = get_object_or_404(Interview, slug=interview_slug)
        current_vacant = get_object_or_404(Vacant, slug=current_interview.vacant.slug)
        current_interview.delete()
        return redirect("vacant", current_vacant.slug)
        #return JsonResponse({"success": "iten delete"}), redirect("vacant", current_vacant.enterprise.slug, current_vacant.slug)



def networking(request, slug_enterprise, pk):
    enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
    networking = NetWorking.objects.get(pk=pk)
    form_netwoking = NetWorkingForm(instance=networking)
    print("here")
    if request.method == "POST":
        # POST
        if "ADD_NETWORKING" in request.POST:
            status = request.POST.get("status")
            name = request.POST.get("name")
            new_networking = NetWorking.objects.create(
                user_added=request.user, status=status, name=name, enterprise=enterprise)
            return redirect("enterprise", slug_enterprise)
        
        elif "SOCIAL_NETWORK" in request.POST:
            set_networking = NetWorkingForm(request.POST, instance=networking)
            if set_networking.is_valid():
                set_networking.save()
                return redirect("networking", slug_enterprise, pk)
        #DELETE
        elif "DELETE_NETWORKING" in request.POST:
            current_networking = get_object_or_404(NetWorking, pk=pk)
            current_networking.delete()
            return redirect("enterprise", slug_enterprise)

        # SET
        elif "SET_SOCIALS_NETWORKING" in request.POST:
            set_socials_networking = NetWorkingForm(request.POST, instance=networking)
            if set_socials_networking.is_valid():
                set_socials_networking.save()
                return redirect("networking", slug_enterprise, pk)
        
        else:
            set_networking = NetWorkingForm(request.POST, instance=networking)
            if set_networking.is_valid():
                set_networking.save()
                return redirect("networking", slug_enterprise, pk)

    ctx = {
        'enterprise': enterprise,
        'networking': networking,
        'form_netwoking': form_netwoking,
    }

    return render(request, "view_networking.html", ctx)


def post_networking(request, vacant_slug):
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)

    if "ADD_NETWORKING" in request.POST:
        current_networking = get_object_or_404(NetWorking, slug=vacant_slug)
        name = request.POST.get("name", "")    
        main_social = request.POST.get("main_social", "")    

        new_networking = NetWorking.objects.create(
            vacant=current_vacant, name=name, main_social=main_social)
        new_networking.save()
        return redirect("vacant", vacant_slug)

    if "DELETE_NETWORKING" in request.POST:
        interview_slug = vacant_slug
        current_networking = get_object_or_404(NetWorking, slug=interview_slug)
        current_networking.delete()
        return redirect("vacant", vacant_slug)
        #return JsonResponse({"success": "iten delete"}), redirect("vacant", current_vacant.enterprise.slug, current_vacant.slug)




# def enterprise(request, slug_enterprise):  # set enterprise detail
#     enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)
#     networking = NetWorking.objects.filter(
#         user_added=request.user, enterprise=enterprise)

#     vacants = Vacant.objects.filter(user_added=request.user, enterprise=enterprise)
#     form_enterprise = EnterpriseForm(instance=enterprise)

#     form_networking = NetWorkingForm()

#     if request.method == 'POST':
#         form_enterprise = EnterpriseForm(request.POST, instance=enterprise)
#         if form_enterprise.is_valid():
#             new_enterprise = form_enterprise.save(commit=False)
#             new_enterprise.user_added = request.user
#             new_enterprise.save()
#             return redirect('enterprise', slug_enterprise)

#     else:
#         ctx = {
#             'form_enterprise': form_enterprise,
#             'enterprise': enterprise,
#             'vacants': vacants,
#             'networking': networking,
#             'form_networking': form_networking
#         }

#         return render(request, 'view_enterprise.html', ctx)

