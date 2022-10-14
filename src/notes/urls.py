from rest_framework import routers

from notes.api import NotesAPIViewSet, CategoriesAPIView

router = routers.DefaultRouter()
router.register('notes', NotesAPIViewSet, 'notes')
router.register('categories', CategoriesAPIView, 'categories')

urlpatterns = router.urls
