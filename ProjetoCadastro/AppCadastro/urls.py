from AppCadastro.views import register, register_create
from django.urls import path

from . import views

app_name = 'AppCadastro'

urlpatterns = [
    path('', views.register, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='create'),
    path('logout/', views.logout_View, name='logout'),

]
