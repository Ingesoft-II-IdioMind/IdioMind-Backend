from rest_framework import routers
from .api import NoteViewset

router=routers.DefaultRouter()
router.register('api',NoteViewset)
urlpatterns=router.urls
