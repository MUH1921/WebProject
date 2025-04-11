from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register_student'),
    path('register/', views.register_student, name='register_student'),
    path('students/', views.view_students, name='view_students'),
]
