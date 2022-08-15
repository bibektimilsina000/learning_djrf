from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "data created sucessfully "}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)

    def update(self, request, pk=None):
        id = pk
        if pk is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        id = pk
        if id is not note:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return response({"msg": "Data updated"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)

    def destroy(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
