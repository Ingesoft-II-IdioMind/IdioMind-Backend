from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()

router.register('api/Accounts', UserViewSet, 'Accounts')

urlpatterns = router.urls
