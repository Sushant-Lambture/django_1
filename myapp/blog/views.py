from django.shortcuts import render, redirect
from .models import Employee,Upload
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

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
def more(request):
    return render(request,'blog/more.html')

def moredata(request):
    btn=request.GET.get('sub')
    id=request.GET.get("eid")
    if btn=="Display":
        record=Employee.objects.get(eid=id)
        param={"data":record}
        return render(request,'blog/more.html',param)

    if btn=='Delete':
        Employee.objects.filter(eid=id).delete()
        param={"msg":"Record Deleted...!!!!"}
        return render(request,'blog/more.html',param)

    if btn=="Edit":
        record=Employee.objects.get(eid=id)
        param={"data":record}
        return render(request,'blog/edit.html',param)

def empupdate(request):
    id=request.GET.get('eid')
    name=request.GET.get('ename')
    loc=request.GET.get('eloc')
    sal=request.GET.get('esal')

    record=Employee.objects.get(eid=id)

    record.ename=name
    record.eloc=loc
    record.esal=sal
    record.save()
    param={"msg":"Record Updated...!!!!!!!"}
    return render(request,'blog/more.html',param)

def delete(request):
    id=request.GET.get('eid')
    Employee.objects.filter(eid=id).delete()
    param={"msg":"Record Deleted!!!!"}
    # return redirect("empform")
    return render(request,'blog/empform.html',param)

def edit(request):
    id = request.GET.get('eid')
    pass
#     record = Employee.objects.get(eid=id)
#     param = {"data": record}
#     return render(request, 'blog/edit2.html', param)
#
# def empupdate2(request):
#     id=request.GET.get('eid')
#     name=request.GET.get('ename')
#     loc=request.GET.get('eloc')
#     sal=request.GET.get('esal')
#
#     record=Employee.objects.get(eid=id)
#
#     record.ename=name
#     record.eloc=loc
#     record.esal=sal
#     record.save()
#     param={"msg":"Record Updated...!!!!!!!"}
#     return render(request,'blog/empform.html',param)

def dropdown (request):
    record = Employee.objects.all()
    param1 = {"data1":record}
    return render(request,'blog/dropdown.html',param1)

# Dropdown and crud
def dropdata(request):
    btn = request.GET.get('sub')
    id = request.GET.get("eid")
    if btn == "Display":
        record = Employee.objects.get(eid=id)
        record1 = Employee.objects.all()
        param = {"data": record, "data1":record1}
        return render(request, 'blog/dropdown.html', param)

    if btn == "Delete":
        Employee.objects.filter(eid=id).delete()
        record1 = Employee.objects.all()
        param ={"msg" : "Record Deleted", "data1":record1}
        return render(request,'blog/dropdown.html',param)


# Image step 2
def add_p(request):
    return render(request, 'blog/product.html')

# Image step 5
def upload(request):
    btn=request.POST.get('sub')
    if btn == "Submit":
        p= Upload()
        p.pname = request.POST.get('pname')
        p.pcat = request.POST.get('pcat')
        p.psubcat = request.POST.get('psubcat')
        p.pprice = request.POST.get('pprice')
        p.pdate = request.POST.get('pdate')
        # p.file = request.POST.get('pdate')
        if len(request.FILES) != 0:
            p.pimage=request.FILES['file']
        p.save()
        param = {"msg" : "File Uploaded...!!!"}
        return render(request,'blog/product.html',param)

    if btn == "Display":
        record=Upload.objects.all()
        param = {"data" : record}
        return render(request,'blog/product.html',param)


# signup step 2
def signup(request):
    return render(request,'blog/signup.html')

# signup step 4
def reguser(request):
    username=request.GET.get("uname")
    password=request.GET.get("password")
    email=request.GET.get("email")
    myuser=User.objects.create_user(username,email,password)
    myuser.save()
    return redirect("loginform")

# signup step 5
def loginform(request):
    return render(request,'blog/loginform.html')

# signup step 7
def loginuser(request):
    uname = request.GET.get('uname')
    password = request.GET.get('password')
    user = authenticate(username=uname,password=password)
    # above line red words indicates table and white defined just above
    if user is not None:
        login(request,user)
        return render(request,'blog/home.html')
    else:
        param= {"msg": "Username or password does not match...!!!"}
        return render(request,'blog/loginform.html',param)

# signup step 10
def logoutuser(request):
    logout(request)
    return redirect('loginform')