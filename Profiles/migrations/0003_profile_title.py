# Generated by Django 4.1.7 on 2023-03-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_training_email_alter_training_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]