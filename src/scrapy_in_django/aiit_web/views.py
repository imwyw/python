from django.http import HttpResponse
from django.shortcuts import render
# from . import models


def index(request):
    list = range(50)
    return render(request, 'index.html', {'data': list})


def detail(request):
    stu = {
        'name': 'jack',
        'age': 12,
        'gender': 'female'
    }
    return render(request, 'detail.html', {'data': stu})



