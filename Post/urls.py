from rest_framework import routers
from .api import PostViewSet,PostViewSetLast10
router = routers.DefaultRouter()

router.register('api',PostViewSet,'post')
router.register('last',PostViewSetLast10,'post_last_ten')

urlpatterns = router.urls
