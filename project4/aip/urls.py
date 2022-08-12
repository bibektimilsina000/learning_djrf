from . import views
from django.urls import path

urlpatterns = [
    path("stu/", views.studentApi),
]
