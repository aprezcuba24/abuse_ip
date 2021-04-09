from app.ipabusers.api.category import CategoryViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)


app_name = "api"
urlpatterns = router.urls
