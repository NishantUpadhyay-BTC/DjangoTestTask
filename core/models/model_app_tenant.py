from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'app_tenant'

    @classmethod
    def get_by_name(cls,name):
        return cls.objects.get(name=name)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        app_label = 'app_tenant'

