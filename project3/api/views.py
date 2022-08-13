from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .serializer import StudentSerializers


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def stuCreate(request):
    if request.method == "POST":

        seralizer = StudentSerializers(data=request.body)

        if seralizer.is_valid():
            seralizer.save()

            data = {"response": "data created sucessfully"}

            return JsonResponse(data, safe=True)
