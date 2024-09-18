from django.test import TestCase, Client
from .models import Room
from .models import Reservation
from hotel_reservation.login.models import Customer, RoomManager
import datetime
from django.urls import reverse
class RoomsTestCases(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='erdey')
        manager=RoomManager.objects.get(username='erdey')
        Room.objects.create(manager=manager,room_no=300,room_type='Single',price=1000,is_available=True,no_of_days_advance=10,start_date='2024-09-20')
        Room.objects.create(manager=manager,room_no=301,room_type='Double',price=1500,is_available=True,no_of_days_advance=10,start_date='2024-09-20')

    def test_room_no(self):
        room1 = Room.objects.get(room_no='300')
        room2 = Room.objects.get(room_no='301')
        self.assertEqual(room1.room_no, '300')
        self.assertEqual(room2.room_no, '301')
    def test_room_type(self):
        room1 = Room.objects.get(room_type='Single')
        room2 = Room.objects.get(room_type='Double')
        self.assertEqual(room1.room_type, 'Single')
        self.assertEqual(room2.room_type, 'Double')
    def test_price(self):
        room1 = Room.objects.get(price=1000)
        room2 = Room.objects.get(price=1500)
        self.assertEqual(room1.price, 1000)
        self.assertEqual(room2.price, 1500)
class BookingTestCases(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='erdey')
        manager=RoomManager.objects.get(username='erdey')
        Customer.objects.create(username='erdey')
        Customer.objects.create(username='erdey')
        Room.objects.create(room_no='300',no_of_days_advance=10,start_date='2024-09-20',manager=manager)
        user=Customer.objects.get(username='erdey')
        user1=Customer.objects.get(username='erdey')
        room=Room.objects.get(room_no='300')
        Reservation.objects.create(user_id=user,room_no=room,amount=1000,start_day='2020-03-10',end_day='2020-03-10')
        Reservation.objects.create(user_id=user1,room_no=room,amount=1500,start_day='2020-03-26',end_day='2020-03-28')

    def test_booking_username(self):
        user=Customer.objects.get(username='vivek')
        booking1 = Reservation.objects.get(user_id=user)
        user1=Customer.objects.get(username='vikas')
        booking2 = Reservation.objects.get(user_id=user1)
        self.assertEqual(booking1.user_id.username, 'erdey')
        self.assertEqual(booking2.user_id.username, 'erdey')
    def test_booking_amount(self):
        booking1 = Reservation.objects.get(amount=1000)
        booking2 = Reservation.objects.get(amount=1500)
        self.assertEqual(booking1.amount, 1000)
        self.assertEqual(booking2.amount, 1500)
    def test_booking_roomManager(self):
        booking = Reservation.objects.get(amount=1500)
        self.assertEqual(booking.room_no.manager.username, 'erdey')
class IndexPageViewTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('index')
    def test_index_view(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'booking/index.html')
