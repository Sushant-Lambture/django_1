from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def empform(request):
    return render(request,'blog/empform.html')

def empdata(request):
    btn=request.GET.get('sub')
    if btn=='Submit':
        id=request.GET.get('eid')
        name=request.GET.get('ename')
        loc=request.GET.get('eloc')
        sal=request.GET.get('esal')
        data=Employee(eid=id,ename=name,eloc=loc,esal=sal)
        data.save()
        param={'msg':"Record Inserted"}
        return render(request,'blog/empform.html',param)

    if btn=='Display':
        record=Employee.objects.all()
        param={'data':record}
        return render(request,'blog/empform.html',param)
