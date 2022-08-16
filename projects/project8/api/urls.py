from django.urls import path
from api import views

urlpatterns = [path("stu/", views.hello_word)]
