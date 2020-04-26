from . import api
from .router import Router

router = Router()
router.register('token', api.TokenViewSet, basename='token')
# router.register('product', api.ProductViewSet, basename='product')
urlpatterns = []
urlpatterns += router.urls