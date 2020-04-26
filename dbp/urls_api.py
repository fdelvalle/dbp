from . import api
from .router import Router

router = Router()
router.register('token', api.TokenViewSet, basename='token')
router.register('category', api.CategoryViewSet, basename='category')
router.register('color', api.ColorViewSet, basename='color')
router.register('product', api.ProductViewSet, basename='product')
router.register('sku', api.SkuViewSet, basename='sku')


urlpatterns = []
urlpatterns += router.urls