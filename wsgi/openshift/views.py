import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('newhome/index.html')

def lawn(request):
    return render_to_response('newhome/index.html')

def services(request):
    return render_to_response('newhome/services.html')

def aboutus(request):
    return render_to_response('newhome/aboutus.html')

def contactus(request):
    return render_to_response('newhome/contactus.html')

def lawnreadmore(request):
    return render_to_response('newhome/lawnreadmore.html')

def satisfactionreadmore(request):
    return render_to_response('newhome/satisfactionreadmore.html')

def testimonialsreadmore(request):
    return render_to_response('newhome/testimonialsreadmore.html')

def mowing(request):
    return render_to_response('newhome/mowing.html')

def shrubs(request):
    return render_to_response('newhome/shrubs.html')

def mulch(request):
    return render_to_response('newhome/mulch.html')
