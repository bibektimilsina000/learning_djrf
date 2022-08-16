from django.urls import path
from crud import views

urlpatterns = [path("stu/", views.student)]
