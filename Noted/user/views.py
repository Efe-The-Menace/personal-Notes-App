from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import reg_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from Notes.models import Note_data
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
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
        
@login_required
def user_profile(request):
    notes = Note_data.objects.filter(user=request.user).order_by('-last_modified')[:5]
    total_notes = Note_data.objects.filter(user=request.user).count()
    return render(request, 'user/user_profile.html',{
                      notes: 'notes',
                   total_notes: 'total_notes'
    })

@login_required
def update_user(request):
    user = request.user     
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('profile')
    else:
        form = UpdateUserForm()        
    return render(request, 'user/update_user.html', {'form': form})