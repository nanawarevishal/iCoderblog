# Generated by Django 4.0.6 on 2022-10-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_profile_email_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='blog_img',
            field=models.ImageField(default='null', upload_to='blog/images'),
        ),
    ]
