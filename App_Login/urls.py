from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('signin/', views.signin_page, name='signin'),
    path('signout/', views.signout_page, name='signout'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/', views.edit_profile_page, name='edit_profile'),
    path('password/', views.change_password_page, name='change_password'),
    path('add_profile_pic/', views.add_profile_picture_page, name='add_profile_pic'),
    path('change_profile_pic/', views.change_profile_picture_page, name='change_profile_pic'),
]