from django import forms
from .models import Account

class RegistrationFrom(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']