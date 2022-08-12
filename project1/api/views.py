from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import studentSerializers
from rest_framework.renderers import JSONRenderer

# one by one
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serilizer = studentSerializers(stu)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data, content_type="application/json")


# queryset all student data
def student_list(request):
    stu = Student.objects.all()
    serilizer = studentSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serilizer.data)
    # return HttpResponse(json_data, content_type="application/json")

    return JsonResponse(serilizer.data, safe=False)
