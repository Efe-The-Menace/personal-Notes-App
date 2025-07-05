from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import reg_form, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from Notes.models import Note_data
from django.contrib.auth.decorators import login_required
from .models import profile_data


def register_user(request):
    if request.method == 'POST':
        form = reg_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created, You can proceed to Log In.')
            return redirect('login')
    else:
        form = reg_form()
    return render(request, 'user/register.html', {'form':form})
    
#Alternative, User defined login view

# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data= request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, f'You are now logged in as {user}')
#             return redirect('note_list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'user/login.html', {'form': form})
    
    # ALternative, User defined Logout view
# def logout_user(request):
#     logout(request)
#     messages.success(request, "You have been logged out.")
#     return redirect('login')
        
@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile_data)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('profile')
        
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile_data)
        
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/user_profile.html', context)