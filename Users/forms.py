from django import forms
from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     """Form for user login."""
#     username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter your username'
#     }))
#     password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter your password'
#     }))

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    """Form for user registration."""
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    password_confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter your password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
        }

    def clean_password_confirm(self):
        """Ensure the password confirmation matches the password."""
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirm

    def clean_username(self):
        """Ensure the username is unique."""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

