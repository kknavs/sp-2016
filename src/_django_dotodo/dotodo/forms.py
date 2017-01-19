from django import forms
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username:'), max_length=100, required=True)
    # email = forms.CharField(label='Email:', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label=_('Password:'), min_length=5, max_length=100, widget=forms.PasswordInput, required=True)
    error_css_class = 'error'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
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
    # newCategory = forms.fields.CharField(label='Name of new category (optional):', required=False) #- separated

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditTaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = _('Name:')
        self.fields['description'].label = _('Description:')
        self.fields['finished'].label = _('Finished:')
        self.fields['date'].label = _('Deadline:')
        self.fields['priority'].label = _('Set priority for task:')
        self.fields['video'].label = _('Add video (optional):')
        self.fields['category'].label = _('Set category (optional):')
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
    category = forms.ModelChoiceField(label=_('Category'), queryset=Category.objects.all(), empty_label=_('*Add new category*'), required=False)
    cat_name = forms.fields.CharField(label=_('Name of category:'), required=False)
    # http://stackoverflow.com/questions/4880842/how-to-dynamically-set-the-queryset-of-a-models-modelchoicefield-on-a-forms-form

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditCategoryForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.request.POST.get('cat_name'):
            kwargs['commit'] = False
            obj = super(EditCategoryForm, self).save(*args, **kwargs)
            if self.request:
                obj.user = self.request.user
            obj.save()
            return obj
        self.add_error('cat_name', _('Name is required field for new category and update.'))
        return None

    class Meta:
        model = Category
        exclude = ['created_date', 'updated_date', 'user']


class EditNotificationsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditNotificationsForm, self).__init__(*args, **kwargs)
        self.fields['priority'].label = _('Set notifications sending through email:')

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(EditNotificationsForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
        obj.save()
        return obj

    class Meta:
        model = Notifications
        exclude = ['user']


class EditUsernameForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
