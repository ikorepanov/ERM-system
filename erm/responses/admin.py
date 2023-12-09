from django.contrib import admin

from .models import (Employer, EmployerContact, JobApplication, Position,
                     Response, ThirdPartyCompany, ThirdPartyContact)


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date_applied',
        'company_name',
        'resume',
        'cover_letter',
    )
    search_fields = ('company_name',)
    list_filter = ('date_applied',)


class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'position',
    )


class EmployerContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'role',
        'email',
        'linkedin',
        'phone',
        'company',
    )


class ThirdPartyCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'website',
    )


class ThirdPartyContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'role',
        'email',
        'linkedin',
        'phone',
        'company',
    )


class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'date',
        'employer',
        'position',
        'employercontact',
        'thirdpartycontact',
        'status',
    )


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(EmployerContact, EmployerContactAdmin)
admin.site.register(ThirdPartyCompany, ThirdPartyCompanyAdmin)
admin.site.register(ThirdPartyContact, ThirdPartyContactAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
