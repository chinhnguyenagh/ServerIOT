from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "SmartHome API",
        default_version='v1',
        description="SmartHome API"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[]
)

router1 = DefaultRouter()
router2 = DefaultRouter()
router1.register('home',HomeAPI,basename='homeupdate')
router2.register('device',DeviceAPI, basename='deviceupdate')
urlpatterns = [
    path('',schema_view.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui'),
    path('',include(router1.urls)),
    # path('home/<int:pk>/',include(router1.urls)),
    path('', include(router2.urls)),
    # path('devide/<int:pk>/',include(router2.urls))
]