from django.shortcuts import render
from django.http import HttpResponse


def mainJsonResponse(request):
    return HttpResponse("{“Message”: “Hello World!”}")
