from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    displayname = forms.CharField(
        max_length=50, required=True, help_text='Name to display on the site')
    email = forms.EmailField(
        required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'displayname', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            if Profile.objects.filter(displayname=self.cleaned_data['displayname']).exists():
                raise forms.ValidationError('Displayname already taken')
            elif User.objects.filter(email=self.cleaned_data['email']).exists():
                raise forms.ValidationError('Email already taken')
            else:
                user.save()
        return user
