from django.contrib.auth.forms import UserCreationForm # 
from .models import User

# from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'email', 'name','password1', 'password2']


