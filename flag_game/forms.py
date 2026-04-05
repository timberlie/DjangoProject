from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите имя пользователя'
        }),
        help_text='Только буквы, цифры и @/./+/-/_.'
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'example@mail.com'
        })
    )
    
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Минимум 8 символов'
        })
    )
    
    password_confirm = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль ещё раз'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        if len(username) < 3:
            raise forms.ValidationError('Имя пользователя должно содержать минимум 3 символа')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Пароль должен содержать минимум 8 символов')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Пароль должен содержать хотя бы одну цифру')
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Пароль должен содержать хотя бы одну заглавную букву')
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        
        return cleaned_data