import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('newhome/index.html')

def lawn(request):
    return render_to_response('newhome/index.html')
