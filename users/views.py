from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, LoginForm
from .models import User

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs:home')  # Replace 'home' with your desired redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blogs:home')  # Replace 'home' with your desired redirect URL
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def view_profiles(request):
    users = User.objects.all()
    return render(request, 'profiles/view_profiles.html', {'users': users})

@login_required
def view_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profiles/view_profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        form = RegistrationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_profile', user.id)
    else:
        user = request.user
        form = RegistrationForm(instance=user)
    return render(request, 'profiles/update_profile.html', {'form': form})

@login_required
def delete_profile(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('view_profiles')