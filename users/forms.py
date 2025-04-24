from django.contrib.auth.models import User
from django import forms
from event.forms import StyledFormMixin
import re
from django.contrib.auth.forms import AuthenticationForm



class Signup_form(StyledFormMixin,forms.ModelForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField( max_length=40, widget=forms.PasswordInput,label="Password")
    confirm_password=forms.CharField(label="Confirm password", max_length=40,widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","confirm_password"]
        
    def clean_email(self):
        email=self.cleaned_data.get("email")
        email_exists=User.objects.filter(email=email).exists()
        
        if email_exists:
            raise forms.ValidationError("Email already exists")
        
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []
        
        if len(password1) < 8:
            errors.append('Password must be at least 8 character long')

        if not re.search(r'[A-Z]', password1):
            errors.append(
                'Password must include at least one uppercase letter.')

        if not re.search(r'[a-z]', password1):
            errors.append(
                'Password must include at least one lowercase letter.')

        if not re.search(r'[0-9]', password1):
            errors.append('Password must include at least one number.')

        if not re.search(r'[@#$%^&+=]', password1):
            errors.append(
                'Password must include at least one special character.')

        if errors:
            raise forms.ValidationError(errors)

        return password1
    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get("password1")
        confirm_password=cleaned_data.get("confirm_password")

        if password1 and confirm_password and password1!=confirm_password:
            raise forms.ValidationError("Password not match")
        
        return cleaned_data
    
class Signin_form(StyledFormMixin,AuthenticationForm):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
    
    