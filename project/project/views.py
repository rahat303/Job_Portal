from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.models import *

def loginPage(req):
    if req.method == "POST":
        user_name=req.POST.get('user_name')
        pass_word=req.POST.get('pass_word')

        user=authenticate(username=user_name,password=pass_word)

        print(user)

        if user:
            print("Under user condition")
            login(req,user)
            messages.success(req,'Login Successful!')
            return redirect("homePage")
        else:
            messages.warning(req,"your username and password is roong")
            return render(req,"auth/loginPage.html")

    return render(req,"auth/loginPage.html")

def signupPage(req):
    if req.method == "POST":
        User_type=req.POST.get("User_type")
        User_name=req.POST.get("User_name")
        Display_name=req.POST.get("Display_name")
        Email=req.POST.get("Email")
        Pass_word=req.POST.get("Pass_word")
        Confirm_password=req.POST.get("Confirm_password")

        if Pass_word == Confirm_password:
            user=CustomUserModel.objects.create_user(
                UserType=User_type,
                username=User_name,
                DisplyName=Display_name,
                email=Email,
                password=Confirm_password,
            )
            if User_type == "recruiters":
                RecruitersProfileModel.objects.create(user=user)
            elif User_type == "jobseekers":
                JobseekersProfileModel.objects.create(user=user)

            messages.success(req,'Registration Successful!')
            return render(req,"auth/loginPage.html")
        else:
            messages.warning(req,'Password not matched!')
            return render(req,"signupPage.html")

    return render(req,"auth/signupPage.html")

def logoutPage(req):
    logout(req)
    messages.success(req,'Logout Successful!')
    return redirect("homePage")

def homePage(req):
    return render(req,"index.html")

@login_required
def userProfile(req):
    return render(req,"users/userProfile.html")

@login_required
def editeProfile(req):
    data=req.user
    if req.method == "POST":
        user_id=req.POST.get("user_id")
        DisplyName=req.POST.get("DisplyName")
        Email=req.POST.get("Email")
        contractnumber=req.POST.get("contractnumber")
        website=req.POST.get("website")

    return render(req,"users/editeProfile.html",{"data":data})

@login_required
def deleteProfile(req):
    myid=req.user.id
    data=CustomUserModel.objects.get(id=myid)
    data.delete()
    return redirect('logoutPage')

@login_required
def addJobPage(req):
    carent_user=req.user
    if carent_user.UserType == "recruiters":
        if req.method == "POST":
            carent_user = req.user
            company_name=req.POST.get("company_name")
            company_title=req.POST.get("company_title")
            company_description=req.POST.get("company_description")
            company_logo=req.FILES.get("company_logo")
            company_location=req.POST.get("company_location")
            job_title=req.POST.get("job_title")
            num_openings=req.POST.get("num_openings")
            category=req.POST.get("category")
            job_description=req.POST.get("job_description")
            qualifications=req.POST.get("qualifications")
            salary=req.POST.get("salary")
            deadline=req.POST.get("deadline")
            data=CreateJobModel(
                user = carent_user,
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
            data.save()
            return redirect("findjobPage")
    return render(req, "content/createJob.html")

@login_required
def findjobPage(req):
    data = CreateJobModel.objects.all()
    return render(req,"content/findJob.html",{"data":data})

@login_required
def allPost(req):
    CU=req.user
    data=CreateJobModel.objects.filter(user=CU)
    return render(req,"content/allPost.html",{"data":data})

@login_required
def deleteJob(req,job_id):
    data=CreateJobModel.objects.get(id=job_id)
    data.delete()
    return redirect("allPost")

@login_required
def editeJob(req,job_id):
    data=CreateJobModel.objects.get(id=job_id)
    carent_user=req.user
    if carent_user.UserType == "recruiters":
        if req.method == "POST":
            carent_user = req.user
            job_id=req.POST.get("job_id")
            company_name=req.POST.get("company_name")
            company_title=req.POST.get("company_title")
            company_description=req.POST.get("company_description")
            company_logo=req.FILES.get("company_logo")
            company_location=req.POST.get("company_location")
            job_title=req.POST.get("job_title")
            num_openings=req.POST.get("num_openings")
            category=req.POST.get("category")
            job_description=req.POST.get("job_description")
            qualifications=req.POST.get("qualifications")
            salary=req.POST.get("salary")
            deadline=req.POST.get("deadline")
            data=CreateJobModel(
                id=job_id,
                user = carent_user,
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
            data.save()
            return redirect("allPost")
    return render(req,"content/editeJob.html",{"data":data})