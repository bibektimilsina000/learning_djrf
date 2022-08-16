from django.urls import path
from crud import views

urlpatterns = [
    path("stu/", views.AllStudents.as_view()),
    path("stu/<int:pk>", views.GUCStudent.as_view()),
]
