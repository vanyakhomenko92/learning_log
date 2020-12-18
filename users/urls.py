"""Определяет схемы URL для пользователей"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from users import views

urlpatterns = [
    url('login/', LoginView.as_view(template_name='users/login.html'),name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    # Страница регистрации
    url(r'^register/$', views.register, name='register'),
]
