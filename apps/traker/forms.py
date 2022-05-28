
from django import forms
from .models import Vacant, Enterprise, Interview, NetWorking, SocialNetworks


class VacantForm(forms.ModelForm):
	class Meta:
		model = Vacant
		fields = ['roll_Name','state','enterprise', 'roll_description', 'feed_back', 'strategy']

class EnterpriseForm(forms.ModelForm):
	class Meta:
		model = Enterprise
		fields = ['name', 'web', 'glassdoor_link', 'summary', 'vision', 'mission']

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