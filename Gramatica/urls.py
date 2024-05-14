from rest_framework import routers
from .api import GrammarViewSet
router = routers.DefaultRouter()

router.register('space',GrammarViewSet,'grammar-phrase')

urlpatterns = router.urls
