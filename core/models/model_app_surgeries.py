from django.db import models
from core.models.model_app_tenant import TenantAwareModel

# Surgery model
class SurgeryModel(TenantAwareModel):
    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, null=True)
    
    class Meta:
        app_label = 'app_surgeries'
    

    def __str__(self):
        return str(self.name)


