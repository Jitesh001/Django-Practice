from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def middlewareTest1(request):
    print("view is executed")
    return HttpResponse("This is view")

def middlewareTest2(request):
    print("excption view is executed")
    num = 10/0
    return HttpResponse("Excpetion Vieeeew")

def middlewareTest3(request):
    print("template respose view is executed")
    context = {'name':'Jitesh'}
    return TemplateResponse(request, 'djangomidleware/sample.html', context)