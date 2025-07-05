from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import profile_data

class reg_form(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        
        model = User
        fields = ['username', 'email']
        
        
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = profile_data
        fields = ['image', 'bio']