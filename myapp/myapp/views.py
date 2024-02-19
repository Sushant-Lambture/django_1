from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'myapp/home.html')
    # return HttpResponse("<h1>Welcome to Home Page</h1> <a href='home'>Home</a> | <a href='about'>About</a> | <a href='contact'>Contact</a>")

def about(request):
    return render(request,'myapp/about.html')
    # return HttpResponse("<h1>Welcome to About Page</h1> <a href='home'>Home</a> | <a href='about'>About</a> | <a href='contact'>Contact</a>")
def contact(request):
    return render(request,'myapp/contact.html')
    # return HttpResponse("<h1>Welcome to Contact Page</h1> <a href='home'>Home</a> | <a href='about'>About</a> | <a href='contact'>Contact</a>")

def person(request):
    return render(request,'myapp/person.html')

def person_data(request):
    fname=request.GET.get("fname")
    lname=request.GET.get("lname")
    age=request.GET.get("age")
    loc=request.GET.get("location")
    # print(fname,lname,age,loc)

    param={"fname":fname,"lname":lname,"age":age,"location":loc}
    # return render(request,'myapp/person.html',param)
    return render(request,'myapp/person_data.html',param)
