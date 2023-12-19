from django.contrib import admin

from .models import Agency, Employer, Contact, Response


class AgencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )


class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )
    # search_fields = ('name',)
    # list_filter = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'company',
    )
    # search_fields = (
    #     'last_name',
    #     'company',
    # )
    # list_filter = (
    #     'last_name',
    #     'company',
    # )


class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'employer',
        'agency',
        'position',
        'cv',
        'letter',
        'created_at',
        'status',
    )
    # search_fields = (
    #     'employer',
    #     'position',
    # )
    # list_filter = (
    #     'employer',
    #     'position',
    # )


admin.site.register(Agency, AgencyAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Response, ResponseAdmin)
