from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def hello_word(request):
    if request.method == "GET":
        return Response({"msg": "hello world"})

    if request.method == "POST":
        print(request.data)
        return Response({"msg": "Thsi is post Request "})
