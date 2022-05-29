from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacantForm, InterviewForm, EnterpriseForm, NetWorkingForm, SocialNetworksForm
from .models import Vacant, Interview, Enterprise, NetWorking, SocialNetworks

from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

# http://127.0.0.1:8000/dashboard/


def dashboard(request):
    vacants = Vacant.objects.filter(user_register=request.user)
    add_vacant_form = VacantForm()
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
    networking = NetWorking.objects.filter(
        user_register=request.user, enterprise=enterprise)

    vacants = Vacant.objects.filter(user_register=request.user, enterprise=enterprise)
    form_enterprise = EnterpriseForm(instance=enterprise)

    form_networking = NetWorkingForm()

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
            'vacants': vacants,
            'networking': networking,
            'form_networking': form_networking
        }

        return render(request, 'view_enterprise.html', ctx)


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
        # CREATE ENTERPRISE
        if 'ADD_ENTERPRISE' in request.POST:
            query = request.POST.get('ADD_ENTERPRISE', '')
            vacant = Vacant.objects.get(slug=vacant_slug)
            enterprise = Enterprise.objects.get_or_create(user_register=request.user, name=query)
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
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug, )
    current_interview = get_object_or_404(Interview, slug=interview_slug)
    interview_form = InterviewForm(instance=current_interview)
    

    if request.method == 'POST':
        # PUT
        interview_form = InterviewForm(
            request.POST, instance=current_interview)
        print(request.POST)
        if interview_form.is_valid():
            new_interview = interview_form.save(commit=False)
            new_interview.user_register = request.user
            new_interview.save()
            return redirect("interview", slug_enterprise, vacant_slug, current_interview.slug)
        else:
            return JsonResponse({"error": "valid2 error"})

    
    ctx = {
        'interview': current_interview,
        'vacant': current_vacant,
        'interview_form': interview_form
    }

    return render(request, "view_interview.html", ctx)


def add_interview(request, vacant_slug):
    current_vacant = get_object_or_404(Vacant, slug=vacant_slug)

    if "ADD_INTERVIEW" in request.POST:
        query_day = request.POST.get("ADD_INTERVIEW", "")
        new_interview = Interview.objects.create(
            vacant=current_vacant, day=query_day)
        new_interview.save()
        return redirect("index")


def networking(request, slug_enterprise, pk):
    enterprise = get_object_or_404(Enterprise, slug=slug_enterprise)

    try:
        networking = NetWorking.objects.get(pk=pk)
    except:
        networking = NetWorking.objects.create(name="algo")
    
    print(networking)

    form_netwoking = NetWorkingForm(instance=networking)

    # social_network = SocialNetworks.objects.get_or_create(networking=networking)

    # form_social_network = SocialNetworksForm(instance=social_network)
    
    if request.method == "POST":
        # POST
        if "ADD_NETWORKING" in request.POST:
            status = request.POST.get("status")
            name = request.POST.get("name")
            new_networking = NetWorking.objects.create(
                user_register=request.user, status=status, name=name, enterprise=enterprise)
            new_networking.save()
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
        else:
            set_networking = NetWorkingForm(request.POST, instance=networking)
            if set_networking.is_valid():
                set_networking.save()
                return redirect("networking", slug_enterprise, pk)

    ctx = {
        'enterprise': enterprise,
        'networking': networking,
        'form_netwoking': form_netwoking,
        # 'form_social_network':form_social_network
    }

    return render(request, "view_networking.html", ctx)
