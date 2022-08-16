# generic api view and model mixins

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class AllStudents(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GUCStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
