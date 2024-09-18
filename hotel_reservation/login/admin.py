from django.contrib import admin
from hotel_reservation.login.models import Customer, RoomManager
from hotel_reservation.reservation.models import Contact, Room, Reservation

# Register your models here.
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Reservation)
