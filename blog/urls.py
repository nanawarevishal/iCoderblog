"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path('postComment',views.postComment,name='postComment'),
 path('',views.index, name = 'index'),

#  path('home',views.home, name = 'home'),

 path('about',views.about, name = 'about'),
 path('category',views.category, name = 'category'),
 path('singlepost/<int:blogID>',views.single_post, name = 'single_post'),
#  path('singlepost',views.single_post, name = 'single_post'),
 path('tags',views.tags,name = 'tags'),
 path('category/<int:catno>',views.category,name='category'),
 path('category/<str:tags>',views.category,name='category'),
 path('category/<str:tags>',views.tags,name = 'category'),
 path('Signup',views.Signup,name='Signup'),
 path('Login',views.Login,name='Login'),
 path('Logout',views.logoutuser,name='Logout'),
 path('sendotp',views.sendotp,name='sendotp'),
 path('otp/<auth_token>',views.otp,name='otp'),
 path('otp',views.otp,name='otp'),
 path('search',views.search,name='search'),
 path('profile',views.profile,name='profile'),
 path('contactus',views.contactus,name='contactus'),
#  path('verify/<auth_token>',views.verify,name="verify"),
  
]
