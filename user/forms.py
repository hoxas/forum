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

    def clean_displayname(self):
        displayname = self.cleaned_data.get('displayname')
        if Profile.objects.filter(displayname=displayname).exists():
            raise forms.ValidationError(
                'Displayname already taken')
        return displayname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already taken')
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)

        if commit:
            user.save()
        return user
