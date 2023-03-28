# Generated by Django 4.1.6 on 2023-03-27 21:49

import accounts.managers
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='Аватар')),
                ('user_info', models.TextField(blank=True, max_length=300, null=True, verbose_name='Информация о пользователе')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Номер телефона')),
                ('gender', models.CharField(choices=[('MAN', 'Мужской'), ('WOMAN', 'Женский')], max_length=100, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
