from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    data = {
        "Name" : "Esteban Mendoza",
        "Track" : "Backend(Python)",
        "Message" : "Hi, mentor, you're doing a great job! Thank you for grading my assignments!"
    }
    return HttpResponse( json.dumps( data ) )