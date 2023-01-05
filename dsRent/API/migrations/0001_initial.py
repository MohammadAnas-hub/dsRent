# Generated by Django 4.0.2 on 2023-01-05 20:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('userId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
                ('phone', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('userImg', models.ImageField(blank=True, null=True, upload_to='accounts/images')),
                ('userType', models.CharField(max_length=50)),
                ('desc', models.TextField(null=True)),
                ('verified', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
    ]
