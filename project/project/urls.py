from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('loginPage',loginPage,name="loginPage"),
    path('signupPage',signupPage,name="signupPage"),
    path('logoutPage',logoutPage,name="logoutPage"),
    path('',homePage,name="homePage"),
    path('userProfile',userProfile,name="userProfile"),
    path('editeProfile',editeProfile,name="editeProfile"),
    path('deleteProfile',deleteProfile,name="deleteProfile"),
    path('addJobPage',addJobPage,name="addJobPage"),
    path('allPost',allPost,name="allPost"),
    path('findjobPage',findjobPage,name="findjobPage"),
    path('deleteJob/<int:job_id>',deleteJob,name="deleteJob"),
    path('editeJob/<int:job_id>',editeJob,name="editeJob"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
