from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['username', 'email']


        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email уже существует')
        return email
    

    def clean(self):
        cleaned_data =super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('Пароли не совпадают')
        return cleaned_data
    
