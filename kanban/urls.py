from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet, SubCardViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'cards', CardViewSet)
router.register(r'subcards', SubCardViewSet)

urlpatterns = router.urls