from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', user_views.login_user, name='login'),  Alternative login URL
    # path('logout/', user_views.logout_user, name='logout'),   Alternatiive Logout URL
    path('profile/', user_views.user_profile, name='profile'),
    path('profile/update', user_views.update_user, name='profile_update'),
]