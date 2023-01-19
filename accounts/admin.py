from django.contrib import admin
from .models import CustomUser,Company,ClientDetails,JobSeeker,UserMedia,Interview,ShortList,RecentlyViewd
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(ClientDetails)
admin.site.register(JobSeeker)
admin.site.register(UserMedia)
admin.site.register(ShortList)
admin.site.register(Interview)
admin.site.register(RecentlyViewd)