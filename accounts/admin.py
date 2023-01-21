from django.contrib import admin
from accounts.models import CustomUser,PersonalInfo,Contact,Education, ShortList,WorkExperiance,UserMedia,ClientDetails,UserMedia,Interview,Company,RecentlyViewd

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(PersonalInfo)
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(WorkExperiance)

admin.site.register(Company)
admin.site.register(ClientDetails)
admin.site.register(UserMedia)
admin.site.register(ShortList)
admin.site.register(Interview)
admin.site.register(RecentlyViewd)