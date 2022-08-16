from django.urls import path
from crud import views

urlpatterns = [
    # path("stu/", views.Students.as_view()),
    # path("stu/", views.ViewAddStudent.as_view()),
    # path("stu/", views.CreateStudent.as_view()),
    # path("stu/<int:pk>", views.EditstdDetail.as_view()),
    # path("stu/<int:pk>", views.GetEditStudent.as_view()),
    # path("stu/<int:pk>", views.GetDeleteStudent.as_view()),
    # path("stu/<int:pk>", views.DeleteStudent.as_view()),
    path("stu/<int:pk>", views.GetUpdateDeleteStudent.as_view()),
]
