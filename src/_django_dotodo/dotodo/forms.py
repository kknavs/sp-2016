from django import forms
from django.contrib.auth import authenticate, login, logout
from .models import Task, Category


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


class DateTypeInput(forms.DateInput):
    input_type = 'date'


class EditTaskForm(forms.ModelForm):
    date = forms.fields.DateField(localize=True, widget=DateTypeInput)
    # newCategory = forms.fields.CharField(label='Name of new category (optional):', required=False) - separate form

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditTaskForm, self).__init__(*args, **kwargs)
        self.fields['priority'].label = 'Set priority for task:'
        self.fields['video'].label = 'Add video (optional):'
        self.fields['category'].label = 'Set category (optional):'
        # http://www.tangowithdjango.com/book/chapters/forms.html

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(EditTaskForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
        obj.save()
        return obj

    class Meta:
        model = Task
        exclude = ['created_date', 'updated_date', 'user']


class EditCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditCategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of new category (optional):'

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(EditCategoryForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
        obj.save()
        return obj

    class Meta:
        model = Category
        exclude = ['created_date', 'updated_date', 'user']
