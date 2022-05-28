
from django import forms
from .models import Vacant, Enterprise, Interview, NetWorking, SocialNetworks


class VacantForm(forms.ModelForm):
	class Meta:
		model = Vacant
		fields = '__all__'

class EnterpriseForm(forms.ModelForm):
	class Meta:
		model = Enterprise
		fields = '__all__'

class InterviewForm(forms.ModelForm):
	class Meta:
		model = Interview
		fields = '__all__'

class NetWorkingForm(forms.ModelForm):
	class Meta:
		model = NetWorking
		fields = '__all__'

class SocialNetworksForm(forms.ModelForm):
	class Meta:
		model = SocialNetworks
		fields = '__all__'