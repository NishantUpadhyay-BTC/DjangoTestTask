from rest_framework import serializers
from core.models.model_app_users import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'full_name', 'created_on', 'update_on', 'email', 'info')
        fields = ['email','username']
