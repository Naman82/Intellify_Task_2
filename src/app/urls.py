from django.urls import path
from app import views

urlpatterns=[
    path('',views.index, name='index'),
    path('student/register/',views.student, name='student'),
    path('teacher/register/',views.teacher, name='teacher'),
    path('student/login/',views.student_login, name='student_login'),
    path('teacher/login/',views.teacher_login, name='teacher_login'),
    path('student/home/',views.student_home, name='student_home'),
    path('teacher/home/',views.teacher_home, name='teacher_home'),
    path('logout/',views.logout,name='logout'),
]