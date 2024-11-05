from django import forms
from .models import Kool,Register

class KoolForm(forms.ModelForm):
    class Meta:
        model = Kool
        fields = ['email','password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','email','password']