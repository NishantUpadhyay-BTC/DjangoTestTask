from rest_framework import routers
from apps.app_surgeries.views import SurgeryViewset
from apps.app_user.views import UsersViewset

router = routers.DefaultRouter()

router.register(r'surgery',SurgeryViewset, basename='surgery')
router.register(r'users', UsersViewset,base_name='users')
urlpatterns = router.urls
