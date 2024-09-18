from rest_framework import viewsets
from hotel_reservation.login.models import Customer
from hotel_reservation.reservation.models import Reservation, Room
from . import serializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.UserSerializer

class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomsSerializer

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = serializers.BookingSerializer