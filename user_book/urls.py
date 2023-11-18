from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    path('', views.home, name = "home"),
    path('entry/id:<str:pk>/', views.entry, name = "person"),
    path('new_entry/interview/id:<str:pk>', views.interview, name = "person"),
    path('interview_viewer/id:<str:pk>', views_admin.interview, name = "interview_viewer"),
    path('interview_manager', views_admin.interview_manager.as_view(), name = "interview_manager"),
]