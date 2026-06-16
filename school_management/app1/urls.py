from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),

]