# import code; code.interact(local=dict(globals(), **locals()))

from django.shortcuts import render
from rest_framework import viewsets
from core.models.model_app_surgeries import SurgeryModel
from core.models.model_app_tenant import Tenant
from .serializer import SurgerySerializer
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404
from apps.app_tenant.utils import set_tenant_schema_for_request
from rest_framework import status

# Create your views here.


class SurgeryViewset(viewsets.ModelViewSet):

    queryset = SurgeryModel.objects.all()
    serializer_class = SurgerySerializer

    def retrieve(self, request, pk=None):
        set_tenant_schema_for_request(self.request)
        tenant_object = Tenant.get_by_name(request.headers.get('Tenant'))
        serializer = SurgerySerializer(tenant_object.surgerymodel_set.filter(pk=pk), many = True)
        return Response(serializer.data)

    def list(self, request , pk=None):
        set_tenant_schema_for_request(self.request)
        tenant_object = Tenant.get_by_name(request.headers.get('Tenant'))
        serializer = SurgerySerializer(tenant_object.surgerymodel_set.all(), many = True)
        return Response(serializer.data)

    def create(self, request , pk=None):
        set_tenant_schema_for_request(self.request)
        tenant = request.headers.get('Tenant')
        tenant_object, created = Tenant.objects.get_or_create(name=tenant)
        req_data = {}
        for key in request.data.keys():
            req_data.update({key:request.data[key]})    
        req_data['tenant'] = tenant_object.id

        serializer = self.get_serializer(data=req_data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        set_tenant_schema_for_request(self.request)
        tenant_object = Tenant.get_by_name(request.headers.get('Tenant'))
        try:
            surgery = tenant_object.surgerymodel_set.get(pk=pk)
            surgery.name = request.data.get('name')
            surgery.save()
            serializer = SurgerySerializer(instance=surgery)
            return Response(serializer.data)
        except:
            return Response({"error":"Object does not exist"})   

    def destroy(self, request, pk=None):
        set_tenant_schema_for_request(self.request)
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(None,status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error":"Object does not exist"},status=status.HTTP_404_NOT_FOUND)   
