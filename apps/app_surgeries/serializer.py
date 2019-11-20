from rest_framework import serializers
from core.models.model_app_surgeries import SurgeryModel

class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryModel
        fields = '__all__'
