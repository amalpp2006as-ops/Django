from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class RegisterForm(forms.ModelForm):
    age = forms.IntegerField()
    file = forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email','password','age','file']

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        
        if not re.match(r"^[a-zA-Z]+$", username):
            raise forms.ValidationError("Username should contain alphabets only.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exists")
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("must be 8 characters long")
        
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
        if not re.match(password_pattern, password):
            raise forms.ValidationError("Password must contain at least one lowercase letter, one uppercase letter, and one digit.")
        return password
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 0:
            raise forms.ValidationError("Age must be a positive integer.")
        return age
    