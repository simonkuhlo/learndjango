from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_keys, name = "all_keys"),
    path('id:<str:pk>/', views.single_key, name = "single_key"),
]