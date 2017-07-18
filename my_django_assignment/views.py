from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('welcome')

def teachers(request):
    return HttpResponse('Here we will show all teachers')
    
def students(request):
    return HttpResponse('Here we will show all students')
    