from django.shortcuts import render, HttpResponse , redirect
from . models import CustomUser
from django.contrib import messages
from . froms import Login_form
from django.contrib.auth import login , authenticate
from django.contrib.auth.hashers import make_password , check_password
# Create your views here.

def Stu_Register(request):
    msg = {}

    if request.method == "POST":
        data = CustomUser()
      
        if request.POST.get("name") == "":
            msg["name_raise"] = "Please Fill This Field"
        

        if request.POST.get("email") == "":
            msg["email_raise"] = "Please Fill This Field"

 
        if request.POST.get("password") == "":
            msg["pass_raise"] = "Please Fill This Field"

        
        if request.POST.get("repassword") == "":
            msg["repass_raise"] = "Please Fill This Field"

        if request.POST.get("repassword") != request.POST.get("password"):
            msg["repass_raise"] = "Both Passwords Dosen`t Matches"


        try:
            email = CustomUser.objects.get(email = request.POST.get("email"))
            msg["dup_email"] = "Email Id Already Exists"
        except:
            
            data.email = request.POST.get("email")


     

        if len(msg)>=1 :
            pass
        
        isparent = request.POST.get('is_parent')
        isstaff = request.POST.get('is_faculty')

        if isparent == 'on':
            if isstaff == 'on':
                isstaff = True
                isparent = True
                print(isparent)
                print(isstaff)
                data.fullname = request.POST.get("name")
                data.password = make_password(request.POST.get("password"))
                # data.cnfrm_passw = request.POST.get("repassword")
                data.is_parent = isparent
                data.is_staff = isstaff
                messages.success(request, "Registration Sucsessfull")
                print(request.POST.get('is_parent'))
                data.save()
                return HttpResponse("Parent and staff both are on")
            else:
                isparent = True
                isstaff = False
                print(isparent)
                print(isstaff)
                data.fullname = request.POST.get("name")
                data.password = make_password(request.POST.get("password"))
                # data.cnfrm_passw = request.POST.get("repassword")
                data.is_parent = isparent
                data.is_staff = isstaff
                messages.success(request, "Registration Sucsessfull")
                print(request.POST.get('is_parent'))
                data.save()
                return HttpResponse("Only parent is On")
            
        elif isstaff == 'on':
                isstaff = True
                isparent = False
                print(isparent)
                print(isstaff)
                data.fullname = request.POST.get("name")
                data.password = make_password(request.POST.get("password"))
                # data.cnfrm_passw = request.POST.get("repassword")
                data.is_parent = isparent
                data.is_staff = isstaff
                messages.success(request, "Registration Sucsessfull")
                print(request.POST.get('is_parent'))
                data.save()
                return HttpResponse("Only Staff is On")
            

        else:
            isparent = False
            isstaff = False
            data.fullname = request.POST.get("name")
            data.password = make_password(request.POST.get("password"))
            data.cnfrm_passw = request.POST.get("repassword")
            data.is_parent = isparent
            data.is_staff = isstaff
            messages.success(request, "Registration Sucsessfull")
            print(request.POST.get('is_parent'))
            data.save()
            return HttpResponse("Both Staff and Parent is Off")
            




    return render(request, "core/register.html", context= {"old_data" : request.POST, "msg" : msg})




def user_login(request):
    frm = Login_form()
    if request.method == "POST":
        frm = Login_form(request=None, data = request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data.get("username")
            passw= frm.cleaned_data.get("password")
            is_parent = frm.cleaned_data.get("is_parent")
            is_staff = frm.cleaned_data.get("is_staff")

            checked_password = request.user.password
            
            usr = authenticate(email = usern, password = passw)
            # pswd = usr.password
            if usr is not None:
                # print(passw)
                if usr.is_parent == True:
                    login(request, usr)
                    # print(usr.password)
                    # return redirect("dashboard")
                    return HttpResponse("This is parent Dashboard")
                elif usr.is_staff == True:
                    login(request, usr)
                    # print(usr.password)
                    # return redirect("dashboard")
                    return HttpResponse("This is Staff Dashboard")
                else:
                    login(request, usr)
                    # print(usr.password)
                    # return redirect("dashboard")
                    return HttpResponse("This is parent Dashboard")
            else:
                print("chal bhakk")
    return render(request, "core/login.html", context={"frm": frm})
