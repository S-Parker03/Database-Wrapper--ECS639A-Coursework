from django.contrib import admin
from .models import Technology, Project, Uses

admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Uses)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'date', 'description']
    search_fields = ['name', 'type']
    list_filter = ['date']


class UsesAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'technology']
    search_fields = ['project', 'technology']
    list_filter = ['project', 'technology']


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id''name', 'type', 'version', 'description']
    search_fields = ['name', 'type']
