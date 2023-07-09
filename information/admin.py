from django.contrib import admin
from .models import UserModel, Coach, Class
# Register your models 


class UserAdmin(admin.ModelAdmin):
    list_display= ("id","full_name","national_code","phone_number","course")

admin.site.register(Class)
admin.site.register(Coach)
admin.site.register(UserModel,UserAdmin)