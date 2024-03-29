from rest_framework import routers

from .views import BrandViewSet, ItemViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')
router.register('products', ProductViewSet, basename='products')
router.register('items', ItemViewSet, basename='items')

urlpatterns = router.urls
