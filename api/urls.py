

from django.urls import path
from . import views


urlpatterns = [

    # for students
    path('students', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    # for employees
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

]