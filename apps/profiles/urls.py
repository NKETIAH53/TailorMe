from rest_framework.routers import DefaultRouter

from .views import UserProfilesViewSet

app_name = "profiles"
router = DefaultRouter()
router.register(r"profiles", UserProfilesViewSet, basename="profiles")

urlpatterns = router.urls
