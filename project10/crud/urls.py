from django.urls import path
from crud import views

urlpatterns = [
    path("stu/", views.StudentList.as_view()),
    # path("stu/", views.StudentCreate.as_view()),
    # path("stu/<int:pk>", views.student),
    # path("stu/<int:pk>", views.RetriveStudent.as_view()),
    # path("stu/<int:pk>", views.updateStudent.as_view()),
    # path("stu/<int:pk>", views.DeleteStudent.as_view()),
]
