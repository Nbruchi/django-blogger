from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profiles/', views.view_profiles, name='view_profiles'),
    path('profile/<int:user_id>/', views.view_user_profile, name='view_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/<int:user_id>/', views.delete_profile, name='delete_profile'),
]