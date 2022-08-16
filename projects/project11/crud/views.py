# generic api view and model mixins

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)


class Students(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudent(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetstdDetail(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EditStudentDetail(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ViewAddStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetEditStudent(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetDeleteStudent(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetUpdateDeleteStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
