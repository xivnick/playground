from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('login', views.login, name='login_page'),
    path('signup', views.signup, name='signup_page'),
]
