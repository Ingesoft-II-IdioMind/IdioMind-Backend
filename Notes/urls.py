from rest_framework import routers
from .api import NoteViewset,DocumentListViewset

router = routers.DefaultRouter()
router.register(r'api/users', NoteViewset, basename='note')
router.register(r'api/document/(?P<documento_id>\d+)', DocumentListViewset, basename='document-notes')
urlpatterns = router.urls
