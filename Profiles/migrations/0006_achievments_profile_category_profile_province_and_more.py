# Generated by Django 4.1.7 on 2023-03-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0005_remove_profile_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=275, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.CharField(max_length=275, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
