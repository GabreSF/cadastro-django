from AppCadastro.views import register, register_create
from django.urls import path

app_name = 'AppCadastro'

urlpatterns = [
    path('', register, name='register'),
    path('create/', register_create, name='create'),
]
