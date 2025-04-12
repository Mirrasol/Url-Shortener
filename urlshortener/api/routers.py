from rest_framework import routers
from .views import URLViewSet

router = routers.DefaultRouter()
router.register(r'urls', URLViewSet, basename='urls')
urlpatterns = router.urls
