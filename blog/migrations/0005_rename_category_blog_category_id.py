# Generated by Django 4.0.6 on 2022-09-25 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='category_id',
        ),
    ]
