from django.urls import path

# Caminho da aplicação recipes função home
from recipes.views import home

urlpatterns = [
    path('', home),  # Home
]
