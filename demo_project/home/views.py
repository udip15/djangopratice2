from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return  HttpResponse("Hello")

# def test(request):
#     return  HttpResponse("Hello Test")
# html filr ma render return garne natra messege lai hhtpresponse garne ani request ni chahinxaa request lai
# def page(request):
#     return render(request ,"test.html")


def index(request):
    return  render(request,'index.html')



def about(request):
    return  render(request,'about.html')


def contact(request):
    return  render(request,'contact.html')