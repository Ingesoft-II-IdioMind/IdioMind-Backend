from rest_framework import routers
from .api import IdiomCreateViewSet

router = routers.DefaultRouter()

router.register('api',IdiomCreateViewSet)

urlpatterns = router.urls