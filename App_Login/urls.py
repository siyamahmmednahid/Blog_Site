from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('signin/', views.signin_page, name='signin'),
]