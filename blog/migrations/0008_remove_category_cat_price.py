# Generated by Django 4.0.6 on 2022-09-25 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_cat_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_price',
        ),
    ]