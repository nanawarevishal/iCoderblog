# Generated by Django 4.0.6 on 2022-10-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('profile_img', models.ImageField(default='static/assets/img/user.jpg', upload_to='blog/images')),
            ],
        ),
    ]
