from rest_framework import routers
from .api import ExamplesViewSet

router=routers.DefaultRouter()
router.register('api',ExamplesViewSet, basename='examples')
urlpatterns=router.urls