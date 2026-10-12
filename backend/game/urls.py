from rest_framework.routers import DefaultRouter
from .views import NodeViewSet, MapViewSet, MapObjectViewSet

router = DefaultRouter()
router.register(r'nodes', NodeViewSet, basename='node')
router.register(r'maps/objects', MapObjectViewSet, basename='map-object')
router.register(r'maps', MapViewSet, basename='map')

urlpatterns = router.urls
