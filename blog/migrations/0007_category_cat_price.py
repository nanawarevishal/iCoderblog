# Generated by Django 4.0.6 on 2022-09-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_cat_category_cat_name_remove_blog_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_price',
            field=models.IntegerField(default=0),
        ),
    ]