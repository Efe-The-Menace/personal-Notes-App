from django.urls import path
from . import views as user_views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )

urlpatterns = [
    path('register/', user_views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', user_views.user_profile, name='profile'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='user/password_reset.html'
             ),
         name='password_reset'),
    
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
             ),
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
             ),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
             ),
         name='password_reset_complete'),
    
]
