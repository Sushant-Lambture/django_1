"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),

    path('empform',views.empform,name='empform'),
    path('empdata', views.empdata, name='empdata'),
    path('more',views.more,name='more'),
    path('moredata',views.moredata,name='moredata'),
    path('empupdate',views.empupdate,name='empupdate'),

    path('delete', views.delete, name='delete'),

    path('edit', views.edit, name='edit'),

    path('dropdown',views.dropdown, name='dropdown'),
    path('dropdata',views.dropdata, name='dropdata'),

# this url is for second sql file ie upload
#     Image step 1
    path('add_p',views.add_p, name='add_p'),

    # Image step 4
    path('upload', views.upload, name='upload'),

    # signup step 1
    path('signup', views.signup, name='signup'),
    path('reguser', views.reguser, name='reguser'),
    path('loginform', views.loginform, name='loginform'),
    path('loginuser', views.loginuser, name='loginuser'),

    # signup step - 9
    path('logoutuser', views.logoutuser, name='logoutuser')
]
