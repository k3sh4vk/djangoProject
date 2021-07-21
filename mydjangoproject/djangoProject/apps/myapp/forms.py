from django import forms
from .models import registrationModel

class registerForm(forms.ModelForm):

    confirm_password = forms.CharField(label='Confirm Password',
                                       widget=forms.PasswordInput()
                                       )
    class Meta:
        model = registrationModel
        fields = '__all__'
        widgets = [

        ]