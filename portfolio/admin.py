from django.contrib import admin
from .models import *


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'execution_link')
    search_fields = ('title',)
    
class ProjectScreenshotAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ('project__title',)

class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)   
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectScreenshot, ProjectScreenshotAdmin)
admin.site.register(Technologies, TechnologiesAdmin)