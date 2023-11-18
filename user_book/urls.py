from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    path('', views.home, name = "home"),
    path('entry/id:<str:pk>/', views.entry, name = "entry"),
    path('new_entry/interview:<str:pk>', views.interview, name = "interview"),
    path('admin/edit_question/id:<str:pk>', views_admin.edit_question, name = "edit_question"),
    path('admin/edit_question/success/', views_admin.edit_question_success, name = "edit_question"),
    path('admin/', views_admin.interview_manager.as_view(), name = "admin"),
]