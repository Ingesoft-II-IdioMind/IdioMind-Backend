from rest_framework import routers
from .api import FlashcardViewset

router=routers.DefaultRouter()
router.register('api',FlashcardViewset)
urlpatterns=router.urls