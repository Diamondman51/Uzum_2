from rest_framework.routers import DefaultRouter

from seller.views import ProductViewSet, PropertyViewSet, QuantityOfProductViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, 'products')
router.register('property', PropertyViewSet, 'property')
router.register('quantity', QuantityOfProductViewSet, 'quantity')

urlpatterns = router.urls
