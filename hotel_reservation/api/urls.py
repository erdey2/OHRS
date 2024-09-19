from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register(r'customer', views.CustomerViewset)
router.register(r'reservation', views.ReservationViewset)
router.register(r'room', views.RoomViewset)
urlpatterns = [
    path('',include(router.urls))
]
