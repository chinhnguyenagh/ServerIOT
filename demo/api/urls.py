from . import views

from django.urls import path

urlpatterns = [
    path('home/<int:pk>',views.UpdateHomeStatus.as_view(),name = 'home'),
    path('devide/<int:devide_id>', views.UpdateStatusDevide.as_view(), name = 'devide')
]