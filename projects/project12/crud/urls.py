from django.urls import path, include
from crud import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("stu", views.StudentViewSet, basename="student")


urlpatterns = [
    path("", include(router.urls)),
]
