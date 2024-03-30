from rest_framework import routers
from .api import PDFDocumentViewSet

router = routers.DefaultRouter()

router.register('api/documents',PDFDocumentViewSet,'documents')


urlpatterns = router.urls