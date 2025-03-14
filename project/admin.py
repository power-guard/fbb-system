from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'resource', 'utility_company', 'image_tag', 'created_at')
    search_fields = ('project_id', 'project_name', 'utility_company', 'address')
    list_filter = ('resource', 'utility_company')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'image_tag')
    inlines = [TaskInline]

    fieldsets = (
        ("Project Info", {
            "fields": (
                'project_id', 'project_name', 'resource', 'image', 'image_tag',
                'capacity_ac', 'capacity_dc', 'utility_company', 'address',
                'longitude', 'latitude', 'altitude'
            )
        }),
        ("Audit Info", {
            "fields": (
                'created_at', 'created_by', 'updated_at', 'updated_by'
            )
        }),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Preview'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'project__project_name')
    list_filter = ('project',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
