from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serilizer import StudentSerilizers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http.response import JsonResponse


def createStd(request):
    if request.method == "GET":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)

        # pythonData = JSONParser().parse(stream)

        # id = stream.get("id", None)
        id = 2
        if id is not None:
            stu = Student.objects.get(id=id)
            serilizer = StudentSerilizers(stu)
            json_data = JSONRenderer().render(serilizer.data)
            return HttpResponse(json_data, content_type="application/json")

        stu = Student.objects.all()
        serilizer = StudentSerilizers(stu, many=True)
        json_data = JSONRenderer().render(serilizer.data)
        return HttpResponse(json_data, content_type="application/json")

    if request.method == "POST":
        json_data = request.body

        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        serilizer = StudentSerilizers(data=python_data)
        if serilizer.is_valid():
            serilizer.save()
            res = {"msg": "Data created"}

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data, content_type="application/json")
