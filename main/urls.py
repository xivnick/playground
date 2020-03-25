from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('login', views.login, name='login_page')
]
