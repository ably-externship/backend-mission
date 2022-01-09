# Generated by Django 3.2 on 2022-01-07 07:17

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=16, verbose_name='비밀번호')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='이메일')),
                ('is_seller', models.BooleanField(default=False, verbose_name='셀러')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='브랜드')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='가입 날짜')),
                ('updated', models.DateField(auto_now=True, verbose_name='업데이트 날짜')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프')),
                ('is_admin', models.BooleanField(default=False, verbose_name='어드민')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='슈퍼유저')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '유저 목록',
                'db_table': 'users',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
