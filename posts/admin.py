from django.contrib import admin
from .models import Post , Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','image','publish','status')
    list_display_links = ('user','status')
    list_filter = ('status','publish')
    search_fields = ('description','status')




admin.site.register(Post,PostAdmin)
admin.site.register(Comment)