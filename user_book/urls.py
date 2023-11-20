from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    path('', views.home, name = "home"),
    path('entry/id:<str:pk>/', views.entry, name = "entry"),
    
    path('new_entry/interview:<str:pk>', views.interview, name = "interview"),
    # path('admin/edit_question/id:<str:pk>', views_admin.edit_question, name = "edit_question"),
    # path('admin/edit_question/success/', views_admin.edit_question_success, name = "edit_question"),
    # path('admin/', views_admin.interview_manager.as_view(), name = "admin"),

    # #New concept
    # path('admin/question/', views_admin.question_list.as_view(), name='question_list'),
    # path('admin/question/add/', views_admin.add_question, name='add_question'),
    # path('admin/question/edit/<int:id>/', views_admin.edit_question, name='edit_question'),
    # path('admin/question/delete/<int:id>/', views_admin.delete_question, name='delete_question'),

    # path('admin/interview/', views_admin.interview_list.as_view(), name='interview_list'),
    # path('admin/interview/add/', views_admin.add_interview, name='add_interview'),
    # path('admin/interview/edit/<int:id>/', views_admin.edit_interview, name='edit_interview'),
    # path('admin/interview/delete/<int:id>/', views_admin.delete_interview, name='delete_interview'),

    # path('admin/entry/', views_admin.entry_list.as_view(), name='entry_list'),
    # path('admin/entry/add/', views_admin.add_entry, name='add_entry'),
    # path('admin/entry/edit/<int:id>/', views_admin.edit_entry, name='edit_entry'),
    # path('admin/entry/delete/<int:id>/', views_admin.delete_entry, name='delete_entry'),

    #approach 2
    path('admin/view/<str:type>', views_admin.list_object, name='object_list'),
    # path('admin/add/<str:type>', views_admin.add_object, name='add_object'),
    # path('admin/edit/<str:type>/<int:id>', views_admin.edit_object, name='edit_object'),
    # path('admin/delete/<str:type>/<int:id>', views_admin.delete_object, name='delete_object'),
]