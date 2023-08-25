from rest_framework.routers import DefaultRouter
from .views import UserViewSet


app_name = "users"
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
