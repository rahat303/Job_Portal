from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import *

def homePage(request):
    return render(request,"index.html")

# <-- add operation -->
@login_required
def createjobPage(request):
    
    if request.method == "POST":
        current_user = request.user
        job_title=request.POST.get("job_title")
        num_openings=request.POST.get("num_openings")
        category=request.POST.get("category")
        job_description=request.POST.get("job_description")
        Required_Skills=request.POST.get("Required_Skills")

        data=CreateJobModel.objects.create(
            user = current_user,
            JobTitle=job_title,
            NumberOfOpenings=num_openings,
            Categry=category,
            JobDescription=job_description,
            RequiredSkills=Required_Skills,
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
    data=CreateJobModel.objects.filter(id=myid)
    data.delete()
    return redirect("findjobPage")

def editePage(request,myid):
    data=CreateJobModel.objects.filter(id=myid)
    if request.method == "POST":
        # current_user = request.user
        JobID=request.POST.get("job_id")
        job_title=request.POST.get("job_title")
        num_openings=request.POST.get("num_openings")
        category=request.POST.get("category")
        job_description=request.POST.get("job_description")
        Required_Skills=request.POST.get("Required_Skills")

        data=CreateJobModel.objects.create(
            # user = current_user,
            id=JobID,
            JobTitle=job_title,
            NumberOfOpenings=num_openings,
            Categry=category,
            JobDescription=job_description,
            RequiredSkills=Required_Skills,
        )
    return render(request,"CRUD/editePage.html",{"data":data})
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
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=CustomUser.objects.create_user(
                UserType=user_type,
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
    return redirect("loginPage")
# </--authentication part -->
