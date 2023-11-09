from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name = "people_list"),
    path('id:<str:pk>/', views.person, name = "person"),
]