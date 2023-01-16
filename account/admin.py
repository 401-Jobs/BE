from django.contrib import admin
from .models import CustomUser,Company,ClientDetails,JobSeeker,UserMedia
# Register your models here.
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_fieldsets=((
        'None',
        {
            'fields':('username','email','password1','password2')
        }
    ),(
        'personal Information',{
            'fields':('first_name','last_name','is_company')
        }
    )
    )
admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(ClientDetails)
admin.site.register(JobSeeker)
admin.site.register(UserMedia)
