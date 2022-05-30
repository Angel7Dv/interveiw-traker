
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
		fields = ['name','position','status','enterprise_opinion','interests','feed_back']

class SocialNetworksForm(forms.ModelForm):
	class Meta:
		model = SocialNetworks
		fields = ['facebook', 'twitter','instagram', 'linkedin', 'web', 'tlf', 'mail',]

	
