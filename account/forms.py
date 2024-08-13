from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    use_required_attribute = False
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'user',
            'placeholder': 'Enter your user name'
        }),
        error_messages={
            'required': 'Username is required.',
        }

    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'register-email',
            'placeholder': 'name@email.com'
        }),
        error_messages={
            'required': 'Email is required.',
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'register-password',
            'placeholder': 'Enter your password'
        }),
        error_messages={
            'required': 'Password is required.',
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'register-password',
            'placeholder': 'Enter your conform'
        }),
        error_messages={
            'required': 'Conform password is required.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    use_required_attribute = False
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'login-user',
            'placeholder': 'Enter your user name'
        }),
        error_messages={
            'required': 'Username is required.',
        }

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'login-password',
            'placeholder': 'Enter your password'
        }),
        error_messages={
            'required': 'Password is required.',
        }
    )
