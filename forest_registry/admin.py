from django.contrib import admin
from .models import (
    WoodSupplier,
    WoodSupplierDocument,
    ForestPlot,
    ForestDocument
)

# ---------- Inline Admins ----------

class WoodSupplierDocumentInline(admin.TabularInline):
    model = WoodSupplierDocument
    extra = 1
    fields = ('document_name', 'document_url')
    readonly_fields = ('uploaded_at',)


class ForestDocumentInline(admin.TabularInline):
    model = ForestDocument
    extra = 1
    fields = ('document_name', 'document_url')
    readonly_fields = ('uploaded_at',)


# ---------- Main Model Admins ----------

@admin.register(WoodSupplier)
class WoodSupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_name', 'project', 'created_at', 'updated_at')
    search_fields = ('name', 'registration_name', 'address')
    list_filter = ['project']
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    inlines = [WoodSupplierDocumentInline]

    fieldsets = (
        ("Supplier Info", {
            "fields": (
                'name', 'registration_name', 'address',
                'registration_document', 'image', 'project', 'user'
            )
        }),
        ("Status & Timestamps", {
            "fields": (
                'created_at', 'created_by',
                'updated_at', 'updated_by'
            )
        }),
    )


@admin.register(ForestPlot)
class ForestPlotAdmin(admin.ModelAdmin):
    list_display = ('registration_name', 'location', 'plot_type', 'wood_supplier', 'created_at', 'updated_at')
    search_fields = ('registration_name', 'location', 'authority')
    list_filter = ['plot_type']
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    inlines = [ForestDocumentInline]

    fieldsets = (
        ("Forest Plot Info", {
            "fields": (
                'registration_name', 'plot_type', 'location', 'registration_date',
                'authority', 'classification', 'removal_method',
                'area', 'distance_from_road', 'forest_document',
                'wood_supplier', 'user'
            )
        }),
        ("Status & Timestamps", {
            "fields": (
                'created_at', 'created_by',
                'updated_at', 'updated_by'
            )
        }),
    )
