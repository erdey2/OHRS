from django.test import TestCase
from .models import Customer
from .models import RoomManager
from hotel_reservation.reservation.models import Reservation, Room
import datetime

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username='tigist',email='tigisthidru@gmail.com', phone_no='0913805096')
        Customer.objects.create(username='ashenafi',email='ashenafitesema@gmail.com', phone_no='0910')
    def test_customer_username(self):
        # I am just trying to take different case to prove the point
        customer1=Customer.objects.get(phone_no='0913805096')
        customer2=Customer.objects.get(username='ashenafi')
        self.assertEqual(customer1.username,'tigist')
        self.assertEqual(customer2.username,'ashenafi')
    def test_customer_email(self):
        customer1=Customer.objects.get(email='tigisthidru@gmail.com')
        customer2=Customer.objects.get(username='ashenafi')
        self.assertEqual(customer1.email,'tigisthidru@gmail.com')
        self.assertEqual(customer2.email,'ashenafitesema@gmail.com')

class RoomManagerTestCase(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='erdey',email='erdeysyoum@gmail.com',phone_no='0914048642')
        RoomManager.objects.create(username='awot',email='awotwelay@gmail.com',phone_no='0914397430')
    def test_roomManager_username(self):
        manager1=RoomManager.objects.get(username='erdey')
        manager2=RoomManager.objects.get(username='awot')
        self.assertEqual(manager1.username,'erdey')
        self.assertEqual(manager2.username,'awot')
    def test_roomManager_email(self):
        manager1=RoomManager.objects.get(email='erdeysyoum@gmail.com')
        manager2=RoomManager.objects.get(email='awotwelay@gmail.com')
        self.assertEqual(manager1.email,'erdeysyoum@gmail.com')
        self.assertEqual(manager2.email,'awotwelay@gmail.com')
    def test_roomManager_phone(self):
        manager1=RoomManager.objects.get(phone_no='0914048642')
        manager2=RoomManager.objects.get(phone_no='0914397430')
        self.assertEqual(manager1.phone_no,'0914048642')
        self.assertEqual(manager2.phone_no,'0914397430')
