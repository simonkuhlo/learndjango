from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('entry/id:<str:pk>/', views.entry, name = "person"),
    path('new_entry/interview/id:<str:pk>', views.interview, name = "person"),
]