from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    TYPE=[
        ("recruiters","Recruiters"),
        ("jobseekers","Jobseekers")
    ]
    UserType=models.CharField(choices=TYPE,max_length=10,null=True)
    DisplyName=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.username}~~{self.UserType}"

class RecruitersProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name="profile1")
    # DisplyName=models.CharField(max_length=100,null=True)
    Bio=models.TextField(max_length=300,null=True)
    ContractNumber=models.CharField(max_length=12,null=True)
    WebLink=models.URLField(null=True)
    Photo=models.ImageField(upload_to="static/Midea/UserPhoto",null=True)

    def __str__(self):
        return f"{self.user.username}~~{self.user.UserType}"

class JobseekersProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name="profile2")
    # DisplyName=models.CharField(max_length=100,null=True)
    Bio=models.TextField(max_length=300,null=True)
    ContractNumber=models.CharField(max_length=12,null=True)
    WebLink=models.URLField(null=True)
    Photo=models.ImageField(upload_to="static/Midea/UserPhoto",null=True)

    def __str__(self):
        return f"{self.user.username}~~{self.user.UserType}"
    
class CreateJobModel(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    com_name = models.CharField(max_length=255,null=True)
    com_title = models.CharField(max_length=255,null=True)
    com_description = models.TextField(null=True)
    com_logo = models.ImageField(upload_to='static/Midea/company_logos',null=True)
    com_location = models.CharField(max_length=255,null=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_listings')
    job_title = models.CharField(max_length=255,null=True)
    num_openings = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=255,null=True)
    job_description = models.TextField(null=True)
    qualifications = models.TextField(null=True)
    salary = models.CharField(max_length=100,null=True)  # Consider using DecimalField for precise salary values
    deadline = models.DateField(null=True)
