from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Marat')

def about(request):
    return HttpResponse('About us')
