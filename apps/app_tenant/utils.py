from django.db import connection
from core.models.model_app_tenant import Tenant

def get_tenants_map():
    return {
        'test':"public",
        "t1": "tenant1_schema",
        "t2": "tenant2_schema",
    }
    
def hostname_from_request(request):
    # split on `:` to remove port
    return request.headers.get('tenant')

def tenant_schema_from_request(request):
    header_flag = hostname_from_request(request)
    tenants_map = get_tenants_map()
    print(header_flag,'************',tenants_map.get(header_flag))
    return tenants_map.get(header_flag)

def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")

def tenant_from_request(request):
    header_flag = hostname_from_request(request)
    # subdomain_prefix = hostname.split('.')[0]
    print('==========',header_flag)
    return Tenant.objects.filter(subdomain_prefix=header_flag).first()