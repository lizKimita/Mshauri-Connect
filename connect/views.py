from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Now you see me now you don't")
