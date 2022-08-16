from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serilizer import StudentSerilizers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)

        pythonData = JSONParser().parse(stream)

        id = pythonData.get("id", None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serilizer = StudentSerilizers(stu)
            # json_data = JSONRenderer().render(serilizer.data)
            # return HttpResponse(json_data, content_type="application/json")
            return JsonResponse(serilizer.data, safe=False)

        stu = Student.objects.all()
        serilizer = StudentSerilizers(stu, many=True)
        # json_data = JSONRenderer().render(serilizer.data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serilizer.data, safe=False)

    def post(self, request, *args, **kwargs):

        json_data = request.body

        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        serilizer = StudentSerilizers(data=python_data)

        if serilizer.is_valid():

            serilizer.save()
            res = {"msg": "Data created"}

            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type="application/json")
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serilizer.errors)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serilizer.errors, safe=False)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id=id)

        serilizer = StudentSerilizers(stu, data=python_data, partial=True)

        if serilizer.is_valid():

            serilizer.save()
            res = {"msg": "data updated"}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type="application/json")
            return JsonResponse(res, safe=False)

        # json_data = JSONRenderer().render(serilizer.errors)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serilizer.errors, safe=False)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg": "Data Deleted !!"}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type="applicatin/json")

        return JsonResponse(res, safe=False)
