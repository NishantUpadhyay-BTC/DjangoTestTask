from django.contrib import admin
from core.models.model_app_surgeries import SurgeryModel
from apps.app_tenant.utils import tenant_from_request
# admin.site.register(SurgeryModel)

@admin.register(SurgeryModel)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tenant']

    # def get_queryset(self, request, *args, **kwargs):
    #     queryset = super().get_queryset(request, *args, **kwargs)
    #     tenant = tenant_from_request(request)
    #     queryset = queryset.filter(tenant=tenant)
    #     return queryset

    # def save_model(self, request, obj, form, change):
    #     tenant = tenant_from_request(request)
    #     obj.tenant = tenant
    #     super().save_model(request, obj, form, change)