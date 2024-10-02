from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    User_Type=[
        ("admin","Admin"),
        ("recuter","Recuter"),
        ("seckeer","Seckeer"),
    ]
    Gender_Type=[
        ("male","Male"),
        ("female","Female")
    ]
    UserType=models.CharField(choices=User_Type,max_length=100,null=True)
    GenderType=models.CharField(choices=Gender_Type,max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    Pic=models.ImageField(upload_to="user_img",null=True)

    def __str__(self):
        return f"{self.username}_{self.UserType}"
    
class CreateJobModel(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    com_name = models.CharField(max_length=255,null=True)
    com_title = models.CharField(max_length=255,null=True)
    com_description = models.TextField(null=True)
    com_logo = models.ImageField(upload_to='company_logos/',null=True)
    com_location = models.CharField(max_length=255,null=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_listings')
    job_title = models.CharField(max_length=255,null=True)
    num_openings = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=255,null=True)
    job_description = models.TextField(null=True)
    qualifications = models.TextField(null=True)
    salary = models.CharField(max_length=100,null=True)  # Consider using DecimalField for precise salary values
    deadline = models.DateField(null=True)

