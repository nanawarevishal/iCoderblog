# Generated by Django 4.0.6 on 2022-10-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_rename_pofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(default=None),
        ),
    ]