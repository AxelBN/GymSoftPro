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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from GymSoftPro import settings
from HealthQuest import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from HealthQuest.views import users_list, physical_evaluation_list_view, Index, payments_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('tables.html/', views.user_view),
    path('users/', users_list.as_view(), name='users_list'),
    path('payments_list/', payments_list.as_view(), name='payments'),
    path('evaluaciones_fisicas', physical_evaluation_list_view.as_view(), name='physical_evaluation'),
    path('physical_evaluations.html', views.physical_evaluation_view    ),
    path('payments_list/update_payments/<int:pk>', views.update_payments.as_view(template_name='HealthQuest/update_payments.html'), name='uptd_payments'),
    path('payments_list/payments.html/', views.payments_view),
    path('users/physical_evaluations.html/', views.physical_evaluation_view),
    path('users/create_users.html/', views.user_view),
    path('users/update.html/<int:pk>', views.updateuser.as_view(template_name='HealthQuest/update.html'), name='updt'),
    path('delete_users.html/<int:pk>', views.deleteuser, name='eliminar'),
    path('update_pe/<int:pk>', views.update_pe.as_view(template_name='HealthQuest/update_pe.html'), name='uptd_pe'),
    path('login/', auth_views.LoginView.as_view(template_name='HealthQuest/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='HealthQuest/login.html'), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)