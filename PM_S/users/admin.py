from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)


# class UserAdmin(admin.ModelAdmin):
#     exclude = ('')


# admin.site.register(User, UserAdmin)


# class Project_docsAdmin(admin.ModelAdmin):
#     list_display = ['name','file', 'description']


# admin.site.register(Project_docs, Project_docsAdmin)