from django.urls import path

# Caminho da aplicação recipes função home
from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]
