from django.contrib import admin

from .models import Company, Position, CV, Template, Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "resp_date",
        "company",
        "position",
        "cv",
        "template",
        "letter",
    )


#    empty_value_display = '-пусто-'


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "description",
    )


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "position",
        "description",
    )


class CVAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "version",
    )


class TemplateAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Response, ResponseAdmin)  # Если убрать ResponseAdmin - в админке отклики будут отображаться списком объектов: одной колонкой, с именем, которое вызывает у объектов метод __str__;
