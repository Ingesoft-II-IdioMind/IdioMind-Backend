from rest_framework import routers
from .api import NoteViewset

router = routers.DefaultRouter()
router.register(r'api', NoteViewset, basename='note')
urlpatterns = router.urls
