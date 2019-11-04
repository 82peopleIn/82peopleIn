from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from userExtends2.forms import UserProfileForm


def auth_login(request, user):
    pass


def register(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.profile.name = form.cleaned_data['name']
        user.profile.email = form.cleaned_data['email']
        user.profile.birthdate = form.cleaned_data['birthdate']
        user.profile.gender = form.cleaned_data['gender']
        user.profile.save()
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'index.html', {'user': user})
    else:
        return render(request, 'registration/register.html', {'form': form, })