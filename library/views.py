from django.shortcuts import render
# from django.core import serializers
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from json import loads, dumps


def index(request):
    return render(request, 'index.html')
