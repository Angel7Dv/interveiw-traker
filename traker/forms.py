
from django import forms
from .models import Vacant


class VacantForm(forms.ModelForm):
	class Meta:
		model = Vacant
		fields = '__all__'
