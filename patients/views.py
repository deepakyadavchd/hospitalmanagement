from django.contrib.auth import authenticate, logout,  login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def patientlogin(request):
    if(request.POST.get("btnlogin")):
       id = request.POST["txtuserid"]
       pwd = request.POST["txtpassword"]
       user = authenticate(username=id,  password=pwd)

       if user:
           login(request, user)  
           username = user.username
           data = {
               "username" : user.username}
           
           return render(request, 'welcome2.html', context=data)

       else:
           data = {
               "error" : "Invalid email and pasword"}
           
           return render(request, 'p_login.html', context=data)
    return render(request, 'p_login.html')

def poutview(request):
    logout(request)
    return redirect("../p_loginpage")

def drlogin(request):
    if(request.POST.get("btnlogin")):
       id = request.POST["txtid"]
       pwd = request.POST["txtpassword"]
       user = authenticate(username=id,  password=pwd)

       if user:
           login(request, user)  
           username = user.username
           data = {
               "username" : user.username}
           
           return render(request, 'welcome.html', context=data)

       else:
           data = {
               "error" : "Invalid email and pasword"}
           
           return render(request, 'd_login.html', context=data)
    
    return render(request,'d_login.html')

def logoutview(request):
    logout(request)
    return redirect("../d_loginpage")

def addpatient(request):
    if(request.POST.get("addbtn")):
        f_name = request.POST["txtfname"]
        l_name = request.POST["txtlname"]
        email_id= request.POST["txtemail"]
        passwd = request.POST["txtpassword"]

        user = User(first_name=f_name, last_name=l_name, email=email_id,
        username=email_id, is_staff=True, is_superuser=True)
        user.set_password(passwd)
        user.save()

        if(request.POST.get("addbtn")):
            mess={"msg": "Patient Added..."}
            return render(request, 'addpatient.html', context=mess)
        
    return render(request,'addpatient.html')
    
def htr(request):
    return render(request,'history.html')
