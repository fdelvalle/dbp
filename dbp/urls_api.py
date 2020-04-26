from . import api
from .router import Router

router = Router()
router.register('token', api.TokenViewSet, basename='token')
router.register('category', api.CategoryViewSet, basename='category')
router.register('color', api.ColorViewSet, basename='color')
router.register('product', api.ProductViewSet, basename='product')
router.register('sku', api.SkuViewSet, basename='sku')

router.register('user', api.UserViewSet, basename='user')
router.register('customer', api.CustomerViewSet, basename='customer')

router.register('order', api.OrderViewSet, basename='order')
router.register('order/item', api.OrderItemViewSet, basename='order_item')


urlpatterns = []
urlpatterns += router.urls