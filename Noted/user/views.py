from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import reg_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = reg_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success('Account created, You can proceed to Log In.')
            return redirect('login')
    else:
        form = reg_form()
    return render(request, 'user/register.html', {'form':form})
    
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'You are now logged in as {user}')
            return redirect('note_list')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
        