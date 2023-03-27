# Generated by Django 4.1.7 on 2023-03-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('second_phone', models.CharField(max_length=50)),
                ('third_phone', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=300)),
                ('instagram', models.URLField(blank=True, max_length=300)),
                ('whatsapp', models.URLField(blank=True, max_length=300)),
                ('allowing', models.BooleanField(default=False)),
            ],
        ),
    ]
