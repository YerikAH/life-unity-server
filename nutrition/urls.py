from rest_framework.routers import DefaultRouter
from .views import NutritionPersonalDetailsViewSet, ValuesConsumedPerDayViewSet

router = DefaultRouter()

router.register(r'nutrition-personal', NutritionPersonalDetailsViewSet)
router.register(r'values-consumed', ValuesConsumedPerDayViewSet)

urlpatterns = router.urls