from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from core.models.model_app_surgeries import SurgeryModel
from core.models.model_app_tenant import Tenant
from rest_framework.authtoken.models import Token
from Multi_Tenant import urls
import os
from django.conf import settings

class SurgeryTest(APITestCase):
    fixtures = ['testdata.json']
    def setUp(self):
        self.data = {
            "name": 'test_11',
        }
        self.client = APIClient()
        self.client.credentials(HTTP_tenant="test")
        self.tetant_data = {
            "name":"test",
            "subdomain_prefix":"foo_bar"
        }
        self.tenant = self.create_tenant(self.tetant_data)
        self.url = reverse('surgery-list')

    @staticmethod
    def create_surgery(data):
        return SurgeryModel.objects.get_or_create(**data)[0]

    @staticmethod
    def create_tenant(data):
        tenant = Tenant.objects.get_or_create(**data)
        return tenant[0]


    def test_surgery_list(self):
        # client = APIClient()
        self.client.credentials(HTTP_tenant="test")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_surgery_create(self):
        tenant = self.create_tenant(self.tetant_data)
        # self.client.credentials(HTTP_tenant= "t1")
        response = self.client.post(self.url, data={"name": "test_surgery", "tenant": tenant.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_surgery_update(self):
        data = {"name":"test_surgery1","tenant":self.create_tenant(self.tetant_data)}
        surgery = self.create_surgery(data)
        url = reverse("surgery-detail",kwargs={"pk":surgery.id})
        response = self.client.put(url,data={"name":"test_surgery_name_changed","tenant":surgery.tenant.id})
        self.assertEqual(response.data.get("name"), "test_surgery_name_changed","Name not changed properly")
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_surgery_delete(self):
        data = {"name": "test_surgery1","tenant": self.create_tenant(self.tetant_data)}
        surgery = self.create_surgery(data)
        url = reverse("surgery-detail", kwargs={"pk": surgery.id})
        response = self.client.delete(url, data={"name": "test_surgery_name_changed"})
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_surgery_delete_does_not_exist(self):
        data = {"name": "test_surgery1",
                "tenant": self.create_tenant(self.tetant_data)}
        surgery = self.create_surgery(data)
        url = reverse("surgery-detail", kwargs={"pk": SurgeryModel.objects.latest('id').id+1})
        response = self.client.delete(
            url, data={"name": "test_surgery_name_changed"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

    
