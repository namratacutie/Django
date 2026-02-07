from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("Hi my name is Lawarna Aree")

def about(respone):
    return HttpResponse("This is my about page")

def contact(response):
    return HttpResponse("This is my contact page.")