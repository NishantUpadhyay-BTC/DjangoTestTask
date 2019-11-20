from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from core.models.model_app_users import User
from . import serializers
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated,SAFE_METHODS,BasePermission

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UsersViewset(viewsets.ModelViewSet):
    """
    This text is the description for this API.

    ---
    parameters:
    - name: username
      description: Foobar long description goes here
      required: true
      type: string
      paramType: form
    - name: password
      paramType: form
      required: true
      type: string
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers

    permission_classes = [IsAuthenticated|ReadOnly]

    # def list(self, request , pk=None):
    #   tenant = request.headers.get('Tenant')
    #   surgeries = SurgeryModel.objects.filter(tenant=tenant)
    #   serializer = SurgerySerializer(surgeries, many = True)
    #   return Response(serializer.data)
    
    def list(self , request,*args,**kwargs):
        """
        Get list of users 
        """
        return super(UsersViewset,self).list(request,args,kwargs)