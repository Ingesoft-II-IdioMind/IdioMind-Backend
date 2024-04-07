from rest_framework import routers
from .api import PDFDocumentListViewSet,PDFDocumentCreateViewSet

router = routers.DefaultRouter()

router.register('api/list',PDFDocumentListViewSet,'documents-list')
router.register('api/create',PDFDocumentCreateViewSet,'documents-create')



urlpatterns = router.urls