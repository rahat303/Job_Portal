from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(RecruitersProfileModel)
admin.site.register(JobseekersProfileModel)
admin.site.register(CreateJobModel)