from rest_framework import routers
from .api import FlashcardViewset,DeckListViewset

router=routers.DefaultRouter()
router.register('api/users',FlashcardViewset, basename='flashcards')
router.register(r'api/deck/(?P<mazo_id>\d+)', DeckListViewset, basename='deck-flashcards')
urlpatterns=router.urls