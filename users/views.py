from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, LoginForm


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=user.profile)
            if profile_form.is_valid():
                profile_form.save()
                if user.is_active:
                    login(request, user)
                return redirect('root')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('root')
            else:
                form.add_error('username', 'Does not exist')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('root')
