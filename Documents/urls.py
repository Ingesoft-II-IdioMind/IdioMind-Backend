from rest_framework import routers
from .api import PDFDocumentListViewSet,PDFDocumentCreateViewSet,TranslateWordViewSet
router = routers.DefaultRouter()

router.register('api/list',PDFDocumentListViewSet,'documents-list')
router.register('api/create',PDFDocumentCreateViewSet,'documents-create')
router.register('api/translate',TranslateWordViewSet,'translate-word')



urlpatterns = router.urls