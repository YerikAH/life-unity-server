from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet, SubCardViewSet

router = DefaultRouter()
router.register('boards', BoardViewSet, basename='boards')
router.register('cards', CardViewSet, basename='cards')
router.register('subcards', SubCardViewSet, basename='subcards')

urlpatterns = router.urls