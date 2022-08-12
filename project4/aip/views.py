from django.shortcuts import render
from .models import *
from .serilizers import StudentSerilizers
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse


def studentApi(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serilizer = StudentSerilizers(stu)
            return JsonResponse(serilizer, safe=False)
        stu = Student.objects.all()

        serilizer = StudentSerilizers(stu, many=True)
        return JsonResponse(serilizer, safe=False)
