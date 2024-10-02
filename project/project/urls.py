from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('',homePage,name="homePage"),
    path('createjobPage',createjobPage,name="createjobPage"),
    path('findjobPage',findjobPage,name="findjobPage"),
    path('deletePage/<str:myid>',deletePage,name="deletePage"),
    path('editePage/<str:myid>',editePage,name="editePage"),
    path('loginPage',loginPage,name="loginPage"),
    path('signupPage',signupPage,name="signupPage"),
    path('logoutPage',logoutPage,name="logoutPage"),
]
