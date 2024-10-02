from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    User_Type=[
        ("admin","Admin"),
        ("recuter","Recuter"),
        ("seckeer","Seckeer"),
    ]
    UserType=models.CharField(choices=User_Type,max_length=100,null=True)

    def __str__(self):
        return f"{self.username}_{self.UserType}"
    
class CreateJobModel(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    JobTitle=models.CharField(max_length=100,null=True)
    NumberOfOpenings=models.PositiveIntegerField(null=True)
    Categry=models.CharField(max_length=100,null=True)
    JobDescription=models.TextField(max_length=1000,null=True)
    RequiredSkills=models.CharField(max_length=100,null=True)
    ApplicationURL=models.URLField(null=True)

