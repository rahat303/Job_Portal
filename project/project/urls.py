from django.contrib import admin
from django.urls import path
from project.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('',homePage,name="homePage"),
    path('createjobPage',createjobPage,name="createjobPage"),
    path('findjobPage',findjobPage,name="findjobPage"),
    path('deletePage/<int:myid>',deletePage,name="deletePage"),
    # path('deletePage2/<str:myid>',deletePage2,name="deletePage2"),
    path('editeJob/<int:myid>',editeJob,name="editeJob"),
    path('allcreatejob',allcreatejob,name="allcreatejob"),
    path('userviewPage',userviewPage,name="userviewPage"),
    path('loginPage',loginPage,name="loginPage"),
    path('signupPage',signupPage,name="signupPage"),
    path('logoutPage',logoutPage,name="logoutPage"),
    path('change_password',change_password,name="change_password"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
