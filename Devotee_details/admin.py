from django.contrib import admin
from .models import DevoteeInfo


admin.site.site_header="ISKCON DEVOTEE DETAILS"
# Register your models here.
class DevoteeAdmin(admin.ModelAdmin):
    list_display = ["legal_name", "initiated_name", "counselor", "mobile_number"]
    search_fields = ["temple_name", "department_name", "legal_name", "initiated_name", "counselor", "mobile_number"]
    list_filter = ["legal_name", "initiated_name", "counselor"]

admin.site.register(DevoteeInfo,DevoteeAdmin)

