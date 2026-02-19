from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'), # Root URL points to home
]
