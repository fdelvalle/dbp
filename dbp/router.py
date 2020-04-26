from collections import OrderedDict

from rest_framework import permissions
from rest_framework import routers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import NoReverseMatch, reverse
from rest_framework.views import APIView

from dbp import urls_api


class Router(routers.DefaultRouter):
    include_root_view = True
    include_format_suffixes = False
    root_view_name = 'index'
    permission_classes = [IsAuthenticated]

    def get_api_root_view(self, api_urls=None):
        return APIRootView.as_view()


class APIRootView(APIView):
    permission_classes = [IsAuthenticated]
    _ignore_model_permissions = True
    exclude_from_schema = True

    def get(self, request, *args, **kwargs):
        ret = OrderedDict()
        namespace = request.resolver_match.namespace
        for key, url_name in self.get_api_root_dict(request).items():
            if namespace:
                url_name = namespace + ':' + url_name
            try:
                ret[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get('format', None)
                )
            except NoReverseMatch:
                continue

        return Response(ret)

    def get_api_root_dict(self, request):
        api_root_dict = OrderedDict()
        list_name = urls_api.router.routes[0].name
        for prefix, viewset, basename in urls_api.router.registry:
            if not request.user.is_staff and permissions.IsAdminUser in viewset.permission_classes:
                continue
            api_root_dict[prefix] = list_name.format(basename=basename)
        return api_root_dict
