from django.contrib import admin
from .models import Technology, Project, Uses

admin.site.register(Technology)
admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'date', 'description']
    search_fields = ['name', 'type']
    list_filter = ['date']
admin.site.register(Uses)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'version', 'description']
    search_fields = ['name', 'type']
# Register your models here.
