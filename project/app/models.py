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
    Bio=models.TextField(max_length=300,null=True)
    ContractNumber=models.PositiveIntegerField(null=True)
    WebLink=models.URLField(null=True)
    Photo=models.ImageField(upload_to="static/Midea/UserPhoto",null=True)

    def __str__(self):
        return f"{self.username}~~{self.UserType}"

class RecruitersProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name="Recruiters_Profile")
    def __str__(self):
        return f"{self.user.username}~~{self.user.UserType}"

class JobseekersProfileModel(models.Model):
    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
    ]
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name="Seekers_Profile")
    Skills=models.CharField(max_length=200,choices=SKILLS,null=True)
    def __str__(self):
        return f"{self.user.username}~~{self.user.UserType}"
    
class CreateJobModel(models.Model):
    Job_Type=[
        ("full_time","Full Time"),
        ("part_time","Part Time")
    ]
    SKILLS = [
        ("programming", "Programming"),
        ("networking", "Networking"),
        ("hardware", "Hardware"),
    ]
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    com_name = models.CharField(max_length=255,null=True)
    com_title = models.CharField(max_length=255,null=True)
    com_description = models.TextField(null=True)
    com_logo = models.ImageField(upload_to='static/Midea/company_logos',null=True)
    com_location = models.CharField(max_length=255,null=True)
    job_title = models.CharField(max_length=255,null=True)
    num_openings = models.PositiveIntegerField(null=True)
    Category = models.CharField(choices=Job_Type,max_length=255,null=True)
    job_description = models.TextField(null=True)
    skills = models.CharField(choices=SKILLS,max_length=200,null=True)
    salary = models.CharField(max_length=100,null=True)  # Consider using DecimalField for precise salary values
    deadline = models.DateField(null=True)

class ApplyModel(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(CreateJobModel,on_delete=models.CASCADE,null=True)
    Cover_Letter=models.TextField(max_length=300,null=True)
    skill=models.CharField(max_length=100,null=True)
    Upload_Resume=models.FileField(upload_to="static/Doc",null=True)
