from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



# user = User.objects.create_user(
#     username="test_user", email="test_user@gmail.com")
# user.set_password("abc123")
# user.save()
