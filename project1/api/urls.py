from django.urls import path
from . import views

urlpatterns = [path("stu/<int:pk>", views.student_detail, name="")]
urlpatterns = [path("stu/", views.student_list, name="")]
