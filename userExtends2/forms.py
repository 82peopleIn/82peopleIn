from django import forms
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.CharField(required=True)
    birthdate = forms.DateField()
    gender = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'birthdate', 'gender',)
