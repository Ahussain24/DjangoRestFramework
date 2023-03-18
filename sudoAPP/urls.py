from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user_authenticate', views.user_authenticate, name='user_authenticate'),
    path('signup_action', views.signup_action, name='signup_action'),
    path('signup', views.signup, name='signup')
]
