# Generated by Django 3.0.2 on 2020-01-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(default='')),
                ('is_superuser', models.BooleanField(default='')),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField(default='')),
                ('is_active', models.BooleanField(default='')),
                ('date_joined', models.DateTimeField(default='')),
                ('last_name', models.CharField(max_length=150)),
            ],
        ),
    ]
