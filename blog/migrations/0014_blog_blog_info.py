# Generated by Django 4.0.6 on 2022-09-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blog_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]