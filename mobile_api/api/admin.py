from django.contrib import admin
from .models import Employer, Store, Visit


class EmployerAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "phone_number")
    search_fields = ("name",)
    empty_value_display = "-empty-"


admin.site.register(Employer, EmployerAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "employer")
    search_fields = ("name",)
    empty_value_display = "-empty-"


admin.site.register(Store, StoreAdmin)


class VisitAdmin(admin.ModelAdmin):
    list_display = ("pk", "store", "date")
    search_fields = ("store__employer__name",)
    empty_value_display = "-empty-"


admin.site.register(Visit, VisitAdmin)
