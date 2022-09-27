from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

# For Sign Up
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



# Edit Profile
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')



# Add Profile Picture
class AddProfilePicture(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)