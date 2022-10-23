import email
import profile
from tkinter import CASCADE
from urllib import request
from venv import create
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     auth_token = models.CharField(max_length=100)
#     # user = models.CharField(max_length=20,null=True,default=None)
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     first_name = models.CharField(max_length=20)
#     last_name= models.CharField(max_length=20,default='null')
#     mobile_no = models.IntegerField(default=0)
#     email = models.EmailField(default='null')
#     profile_img = models.ImageField(upload_to ='blog/images',default='')


#     def __str__(self):
#         return self.user.username

class Profile(models.Model):
    user =models.CharField(max_length=20)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=10,default=None)
    last_name = models.CharField(max_length=20,default=None)
    mobile_no = models.IntegerField(default=None)
    email = models.EmailField(default=None)
    profile_img = models.ImageField(upload_to ='blog/images',default='static/assets/img/user.jpg')

    def __str__(self):
        return self.user
    

class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=50)


    def __str__(self):
        return self.cat_name


class blog(models.Model):
    blog_id = models.IntegerField(default=0,primary_key=True)
    cat_num = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    date = models.DateField()
    blog_desc = models.TextField()
    blog_info = models.TextField()
    tags = models.CharField(max_length=50)
    blog_img = models.ImageField(upload_to ='blog/images',default='null')
    author = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:13]+"...."+"by "+self.user.username


class ContactUS(models.Model):
    name = models.CharField(max_length=20)
    email=models.EmailField()
    subject =models.CharField(max_length=50)
    msg = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
