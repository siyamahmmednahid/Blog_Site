from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# For Sign Up
def signup_page(request):
    form = UserCreationForm()

    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
        else:
            print(form.errors)

    return render(request, 'App_Login/signup.html', {'form': form, 'registered': registered})



# For Sign In
def signin_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Blog:blogs'))
        else:
            print(form.errors)

    return render(request, 'App_Login/signin.html', {'form': form})



# For Sign Out
@login_required
def signout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:signin'))