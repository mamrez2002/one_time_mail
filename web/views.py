from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def write_mail(requests):
    return HttpResponse('hello world')