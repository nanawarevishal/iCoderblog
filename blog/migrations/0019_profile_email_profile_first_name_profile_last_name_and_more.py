# Generated by Django 4.0.6 on 2022-10-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
