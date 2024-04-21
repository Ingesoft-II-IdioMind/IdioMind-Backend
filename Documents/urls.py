from rest_framework import routers
from .api import PDFDocumentCreateViewSet,TranslateWordViewSet
router = routers.DefaultRouter()

router.register('api',PDFDocumentCreateViewSet,'documents-create')
router.register('translate',TranslateWordViewSet,'translate-word')



urlpatterns = router.urls