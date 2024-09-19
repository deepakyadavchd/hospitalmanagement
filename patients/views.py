from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')



def patientlogin(request):
    
    # if(request.POST.get("btnlogin")):
    #    userid = request.POST["txtuserid"]
    #    passwprd = request.POST["txtpassword"]
    #    user = authenticate(username=userid,  password=passwprd)

    #    if user:
    #        login(request, user)   # to store userid in session
    #        username = user.username
    #        data = {
    #            "username" : user.username
    #        }
    #        return render(request, 'welcome.html', context=data)
    #    else:
    #        data = {
    #            "error" : "Invalid email and pasword"}
    #        return render(request, 'p_login.html', context=data)
    return render(request, 'p_login.html')


def doctorlogin(request):
    
    if(request.POST.get("btnlogin")):
       dr_id = request.POST["txtid"]
       passwd = request.POST["txtpassword"]
       user = authenticate(username=dr_id,  password=passwd)

       if user:
           login(request, user)  
           username = user.username
           data = {
               "username" : user.username
           }
           
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
            mess={"msg": "Congratulations, your account has been successfully created ."}
            return render(request, 'addpatient.html', context=mess)
        


    return render(request,'addpatient.html')
    
