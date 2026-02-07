from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.

# def index(request):
#     return  HttpResponse("Hello")

# def test(request):
#     return  HttpResponse("Hello Test")
# html filr ma render return garne natra messege lai hhtpresponse garne ani request ni chahinxaa request lai
# def page(request):
#     return render(request ,"test.html")


def index(request):
    data = {
        "name" : "Something",
        "users" : [
            {
                "name" : "Himal",
                "photo" : "https://img.freepik.com/free-photo/portrait-confident-young-businessman-with-his-arms-crossed_23-2148176206.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "name" : "Sandesh",
                "photo" : "https://img.freepik.com/free-photo/portrait-white-man-isolated_53876-40306.jpg?semt=ais_hybrid&w=740&q=80"
            }
        ]
    } 
    return  render(request,'index.html', data)



def about(request):
    return  render(request,'about.html')


def contact(request):
    blogs = Blog.objects.all()
    data = {
        "blogs" : blogs
    }



    return  render(request,'contact.html',data)

def ourmerch(request):
    return  render(request,'ourmerch.html')


def submit(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')

    Blog.objects.create(title=name, info=email)


    # with open('file.csv', 'a+') as f:
    #     f.write(f"{name},{email},{contact}\n")
        
    return HttpResponse("ok")