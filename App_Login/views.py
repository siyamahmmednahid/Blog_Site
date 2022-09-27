from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, EditProfileForm, AddProfilePicture


# Create your views here.

# For Sign Up
def signup_page(request):
    form = SignUpForm()

    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
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
                return HttpResponseRedirect(reverse('App_Login:profile'))
        else:
            print(form.errors)

    return render(request, 'App_Login/signin.html', {'form': form})



# For Sign Out
@login_required
def signout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:signin'))



# For Profile
@login_required
def profile_page(request):
    return render(request, 'App_Login/profile.html')



# For Edit Profile
@login_required
def edit_profile_page(request):
    current_user = request.user
    form = EditProfileForm(instance=current_user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        else:
            print(form.errors)

    return render(request, 'App_Login/edit_profile.html', {'form': form})



# For Change Password
@login_required
def change_password_page(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)

    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        else:
            print(form.errors)

    return render(request, 'App_Login/change_password.html', {'form': form})



# For Add Profile Picture
@login_required
def add_profile_picture_page(request):
    form = AddProfilePicture()

    if request.method == 'POST':
        form = AddProfilePicture(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        else:
            print(form.errors)

    return render(request, 'App_Login/add_profile_picture.html', {'form': form})



# For Change Profile Picture
@login_required
def change_profile_picture_page(request):
    form = AddProfilePicture(instance=request.user.user_profile)

    if request.method == 'POST':
        form = AddProfilePicture(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        else:
            print(form.errors)

    return render(request, 'App_Login/add_profile_picture.html', {'form': form})