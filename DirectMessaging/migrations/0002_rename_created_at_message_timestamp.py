# Generated by Django 4.1.7 on 2023-02-28 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DirectMessaging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='timestamp',
        ),
    ]
