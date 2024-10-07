from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import *


from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


def homePage(request):
    return render(request,"index.html")

# <-- add operation -->
@login_required
def createjobPage(request):
    carent_user=request.user
    if carent_user.UserType == "recuter":
        if request.method == "POST":
            current_user = request.user
            company_name=request.POST.get("company_name")
            company_title=request.POST.get("company_title")
            company_description=request.POST.get("company_description")
            company_logo=request.FILES.get("company_logo")
            company_location=request.POST.get("company_location")
            job_title=request.POST.get("job_title")
            num_openings=request.POST.get("num_openings")
            category=request.POST.get("category")
            job_description=request.POST.get("job_description")
            qualifications=request.POST.get("qualifications")
            salary=request.POST.get("salary")
            deadline=request.POST.get("deadline")
            data=CreateJobModel.objects.create(
                user = current_user,
                com_name=company_name,
                com_title=company_title,
                com_description=company_description,
                com_logo=company_logo,
                com_location=company_location,
                job_title=job_title,
                num_openings=num_openings,
                category=category,
                job_description=job_description,
                qualifications=qualifications,
                salary=salary,
                deadline=deadline,
            )
        return redirect("findjobPage")

    return render(request,"core_conten/createjobPage.html")

def findjobPage(request):
    current_user = request.user

    data = CreateJobModel.objects.all()
    return render(request,"core_conten/findjobPage.html",{"data":data})
# </-- add operation -->


# <-- frood delete, edite operation -->
def deletePage(request,myid):
    data=CreateJobModel.objects.get(id=myid)
    data.delete()
    return redirect("findjobPage")

# def deletePage2(request,myid):
#     data=CreateJobModel.objects.get(id=myid)
#     data.delete()
#     return redirect("allcreatejob")

def editeJob(request,myid):
    data=CreateJobModel.objects.get(id=myid)
    carent_user=request.user
    if carent_user.UserType == "recuter":
        if request.method == "POST":
            current_user = request.user
            company_name=request.POST.get("company_name")
            company_title=request.POST.get("company_title")
            company_description=request.POST.get("company_description")
            company_logo=request.FILES.get("company_logo")
            company_location=request.POST.get("company_location")
            job_title=request.POST.get("job_title")
            num_openings=request.POST.get("num_openings")
            category=request.POST.get("category")
            job_description=request.POST.get("job_description")
            qualifications=request.POST.get("qualifications")
            salary=request.POST.get("salary")
            deadline=request.POST.get("deadline")
            data=CreateJobModel.objects.create(
                user = current_user,
                com_name=company_name,
                com_title=company_title,
                com_description=company_description,
                com_logo=company_logo,
                com_location=company_location,
                job_title=job_title,
                num_openings=num_openings,
                category=category,
                job_description=job_description,
                qualifications=qualifications,
                salary=salary,
                deadline=deadline,
            )
            return redirect("findjobPage")
    return render(request,"CRUD/editeJob.html",{"data":data})

def userviewPage(request):
    return render(request, "authentication/user/userviewPage.html")

def allcreatejob(request):
    current_user = request.user

    data = CreateJobModel.objects.all()
    return render(request, "CRUD/allcreatejob.html",{"data":data})
# </-- frood delete, edite operation -->


# <--authentication part -->
def loginPage(request):
    if request.method=="POST":
        UserName=request.POST.get("user_name")
        Password=request.POST.get("password")
        user=authenticate(username=UserName,password=Password)

        if user:
            login(request,user)
            return redirect("homePage")
        else:
            HttpResponse("Your user info is rong")
    return render(request,"authentication/loginPage.html")

def signupPage(request):
    if request.method=="POST":
        user_type=request.POST.get('user_type')
        gender=request.POST.get('gender')
        City=request.POST.get('City')
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=CustomUser.objects.create_user(
                UserType=user_type,
                GenderType=gender,
                City=City,
                Pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                username=user_name,
                email=email,
                password=confirm_password,
            )
            return redirect("loginPage")
        else:
            return HttpResponse('error')
    return render(request,"authentication/signupPage.html")

def logoutPage(request):
    logout(request)
    return redirect("homePage")

# </--authentication part -->


def change_password(request):
    current_user = request.user
    if request.method == "POST":
            old_password=request.POST.get("current_password")
            new_password=request.POST.get("new_password")
            confirm_password=request.POST.get("confirm_password")
            
            if check_password(old_password, current_user.password):
                
                if old_password == new_password:
                    return HttpResponse("You can't use old password again!")
                
                elif new_password==confirm_password:
                    current_user.set_password(new_password)
                    current_user.save()

                    update_session_auth_hash(request,current_user)

                    return redirect("homePage")
                else:
                    return HttpResponse("password not match")
            else:
                return HttpResponse("old password not match")

    return render(request,"authentication/user/changePassword.html")
