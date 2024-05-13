from rest_framework import routers
from .api import ExamplesViewSet,FeedbackViewSet

router=routers.DefaultRouter()
router.register('api',ExamplesViewSet, basename='examples')
router.register('feedback',FeedbackViewSet, basename='feedback')
urlpatterns=router.urls