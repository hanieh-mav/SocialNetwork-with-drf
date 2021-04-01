from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Friend

# Register your models here.

UserAdmin.fieldsets[1][1]['fields'] = ('avatar','first_name', 'last_name', 'email','bio')
admin.site.register(User,UserAdmin)


class FriendAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user')


admin.site.register(Friend,FriendAdmin)