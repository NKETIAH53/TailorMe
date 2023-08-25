from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.profiles.urls", namespace="profiles")),
    path("", include("apps.users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "TailorMe"
admin.site.site_title = "TailorMe Admin Portal"
admin.site.index_title = "Welcome to the TailorMe Portal"
