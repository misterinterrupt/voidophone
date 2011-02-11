from django.http import HttpResponse
from django.shortcuts import render_to_response
from xml.dom import minidom
def index(response):
    return HttpResponse("Call Index")
    
def listen(response):
    return render_to_response("call/hello.xml")