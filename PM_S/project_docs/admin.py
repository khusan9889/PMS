from django.contrib import admin
from .models import Project_docs
# Register your models here.


admin.site.register(Project_docs)

# class Project_docsAdmin(admin.ModelAdmin):
#     list_display = ['name','file', 'description']


# admin.site.register(Project_docs, Project_docsAdmin)