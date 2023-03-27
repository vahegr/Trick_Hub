# Generated by Django 4.1.7 on 2023-03-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users')),
                ('bio', models.TextField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True, unique=True)),
                ('github', models.URLField(blank=True, null=True, unique=True)),
                ('linkedin', models.URLField(blank=True, null=True, unique=True)),
                ('twitter', models.URLField(blank=True, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]