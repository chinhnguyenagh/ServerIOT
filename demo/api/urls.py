from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router2 = DefaultRouter()
router1.register('home',HomeAPI,basename='homeupdate')
router2.register('device',DeviceAPI, basename='deviceupdate')
urlpatterns = [
    path('home/',include(router1.urls)),
    path('home/<int:pk>/',include(router1.urls)),
    path('device/', include(router2.urls)),
    path('devide/<int:pk>/',include(router2.urls))
]