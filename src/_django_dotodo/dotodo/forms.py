from django import forms
from django.contrib.auth import authenticate, login, logout


class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100, required=True)
    # email = forms.CharField(label='Email:', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password:', min_length=5, max_length=100, widget=forms.PasswordInput, required=True)
    error_css_class = 'error'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
            # self.add_error('password', 'Sorry, that login was invalid. Please try again..')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
