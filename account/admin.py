from django.contrib import admin
from account.models import MyUser, UserTypeCategory

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'is_verified')
    

@admin.register(UserTypeCategory)
class UserTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_type')