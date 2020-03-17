from django.shortcuts import render, HttpResponse, redirect
from backend_app.forms import CollegeUserBasicInfoForms
from django.contrib.auth.hashers import make_password,check_password
from misc_files.generic_functions import generate_string,verify_mail_send
from backend_app.models import UserRole,CollegeUserBasicInfo


def index_page(request):
    return render(request, "index.html")


def signup_page(request):
    if request.method == "POST":
        detail_form = CollegeUserBasicInfoForms(request.POST)
        if detail_form.is_valid():
            form = detail_form.save(commit=False)  # variable form and save when valid
            form.name = request.POST['name']
            form.email = request.POST['email']
            form.password = make_password(request.POST['password'])
            form.gender = request.POST['gender']
            form.mobile = request.POST['mobile']
            form.role_id = UserRole.objects.get(role_name="colleger").role_id
            string = make_password(generate_string()).replace("+", "")
            full_link = r"127.0.0.1:8000/verify/?token={}".format(string)
            form.verify_link = string
            form.save()
            verify_mail_send(request.POST['email'], request.POST['name'], full_link)
            return redirect('/')
        else:
            return HttpResponse("error")

    return render(request,"front_master_page.html")





def verify_link(request):
    try:
        token= request.GET['token']
    except Exception as error:
        return HttpResponse("invalid{}".format(error))
    else:
        data =CollegeUserBasicInfo .objects.filter(verify_link = token).exists()
        if data is True:
            update = CollegeUserBasicInfo(email=CollegeUserBasicInfo.objects.get(verify_link = token).email,verify_link="",is_active=1)
            update.save(update_fields=['verify_link', 'is_active'])
            return redirect('/')

        else:
            return HttpResponse("Invalid Token.")


def signin_page(request):
    if request.method =="POST":
        if CollegeUserBasicInfo.objects.filter(email=request.POST['email']).exists() is True:
            data= CollegeUserBasicInfo.objects.get(email=request.POST['email'])
            if check_password(request.POST['password'],data.password):
                if data.is_active== 1:
                    if data.role.role_name == "colleger":
                        return redirect("/index.html/")
                else:
                 if data.verify_link!="":
                    return render(request,"front_master_page.html",{'verify_email':True})
                 else:
                    return render(request,"front_master_page.html",{'permision denied':True})
            else:
                return render(request,"front_master_page.html",{'invalid_password':True})
        else:
            return render(request,"front_master_page.html",{'invalid_email':True})
    return render(request,"front_master_page.html")