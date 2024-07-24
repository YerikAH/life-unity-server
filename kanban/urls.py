from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet, SubCardViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename='boards')
router.register(r'cards', CardViewSet, basename='cards')
router.register(r'subcards', SubCardViewSet, basename='subcards')

urlpatterns = router.urls