from rest_framework import routers
from .api import DeckViewset

router=routers.DefaultRouter()
router.register('api',DeckViewset)
urlpatterns=router.urls