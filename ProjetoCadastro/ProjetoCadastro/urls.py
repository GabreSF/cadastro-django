from AppCadastro.views import register
from django.urls import path

urlpatterns = [
    path('', register, name='register'),
]
