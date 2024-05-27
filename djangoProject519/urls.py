"""
URL configuration for djangoProject519 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list/', views.depart_list, name='depart_list'),
    path('depart/add/', views.depart_add, name='depart_add'),
    path('depart/delete/', views.depart_delete, name='depart_delete'),
    re_path(r'depart/(?P<nid>\d+)/edit/', views.depart_edit, name='depart_edit'),

    # 用户管理
    path('user/list/',views.user_list, name='user_list'),
    path('user/add/',views.user_add,name='user_add'),

    # 编辑用户
    re_path(r'user/(?P<nid>\d+)/edit/', views.user_edit, name='user_edit'),
    re_path(r'user/(?P<nid>\d+)/delete/', views.user_delete, name='user_delete')
]
