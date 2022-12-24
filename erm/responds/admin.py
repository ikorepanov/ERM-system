from django.contrib import admin

from .models import Respond, Company, Position, CV, Template


class RespondAdmin(admin.ModelAdmin):
    list_display = (
        'resp_date',
        'company',
        'position',
        'cv',
        'template',
    )


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class CVAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class TemplateAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


admin.site.register(Respond, RespondAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(Template, TemplateAdmin)
