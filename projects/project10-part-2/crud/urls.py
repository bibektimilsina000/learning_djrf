from django.urls import path
from crud import views

urlpatterns = [
    path("stu/", views.LCstudentAPI.as_view()),
    path("stu/<int:pk>", views.RUDstudetAPI.as_view()),
]
