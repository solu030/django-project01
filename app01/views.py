from django.shortcuts import render,HttpResponse,redirect
from app01.models import UserInfo

# Create your views here.
def index(request):
    return HttpResponse("welcome to django!")

def user_list(request):
    return render(request,"user_list.html" )

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username == 'admin' and password == '123':
        return redirect("https://www.bilibili.com/")

    return render(request,"login.html" ,{"error":"请重新输入"})

def cdus(request):
    # UserInfo.objects.create(name = "哈哈哈" ,password = "2156" , age = 88)
    # UserInfo.objects.filter(id = 1).delete()
    # UserInfo.objects.filter(id = 1).update(name = "rr" ,password = "51554" , age = 44)
    # UserInfo.objects.all()
    return HttpResponse("successful!")

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    
    usr = request.POST.get("usr")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name = usr,password = pwd,age = age)
    return redirect("/info_list/")

def info_list(request):
    data_list = UserInfo.objects.all()

    return render(request,"info_list.html",{"data_list" : data_list})

def info_delete(request):
    uid = request.GET.get("uid")
    UserInfo.objects.filter(id = uid).delete()
    return redirect("/info_list/")
