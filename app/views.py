from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python(request):
    return HttpResponse('python is high level opensource interpreted scripting language ')
def sql(request):
    return HttpResponse('sql is structured quary language which is date stored date in the form of tables')
