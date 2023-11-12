from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('id:<str:pk>/', views.entry, name = "person"),
]