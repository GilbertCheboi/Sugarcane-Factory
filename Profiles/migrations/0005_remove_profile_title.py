# Generated by Django 4.1.7 on 2023-03-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0004_alter_profile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]
