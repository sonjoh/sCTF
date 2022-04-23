from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from users.models import Users
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']
