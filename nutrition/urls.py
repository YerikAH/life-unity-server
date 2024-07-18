from rest_framework.routers import DefaultRouter
from .views import NutritionPersonalDetailsViewSet, ValuesConsumedPerDayViewSet, ValuesRecommendedPerDayViewSet

router = DefaultRouter()

router.register(r'nutrition-personal', NutritionPersonalDetailsViewSet)
router.register(r'values-consumed', ValuesConsumedPerDayViewSet)
router.register(r'values-recommended', ValuesRecommendedPerDayViewSet)

urlpatterns = router.urls

    # "id_user":6,
    # "carbs":100,
    # "protein":20,
    # "fat":50,
    # "cal":10,
    # "water":2