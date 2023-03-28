from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Логин'
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )


class CustomUserCreationForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('MAN', "Мужской"),
        ('WOMAN', "Женский"),
    )

    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Повторите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Пол')

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
            'avatar',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'user_info',
            'phone',
            'gender'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароль не совпадает')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
            'avatar',
            'first_name',
            'last_name',
            'user_info',
            'phone',
            'gender'
        )
        labels = {'email': 'Почта',
                  'username': 'Логин',
                  'avatar': 'Фото профиля',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'user_info': 'Информация о пользователе',
                  'phone': 'Номер телефона',
                  'gender': 'Пол'
                  }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")
