from django.urls import path

from HealthQuest.views import users_list

urlpatterns = [
    path('users/', users_list.as_view(), name='article-list'),
]
