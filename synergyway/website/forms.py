from django import forms
from .models import User, Group


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'group']


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
