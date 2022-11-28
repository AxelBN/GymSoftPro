"""GymSoftPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from HealthQuest import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from HealthQuest.views import users_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('tables.html/', views.user_view),
    path('users/', users_list.as_view(), name='article-list'),
    path('users/create_users.html/', views.user_view),
    path('users/physical_evaluations.html/', views.physical_evaluation_view)
]

urlpatterns += staticfiles_urlpatterns()