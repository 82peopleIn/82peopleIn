from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import redirect, render

from userExtends.forms import ProfileForm, UserForm


def register(request):
    if request.method =="POST":
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': profileForm})
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        return render(request, 'registration/register.html',{'userForm': userForm, 'profileForm': profileForm})


# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             # messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'registration/regiser.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })