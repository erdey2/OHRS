from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('reserve',views.reservation(),name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('reserve-now/<str:id>',views.reserve_now,name='reserve-now'),
    path('cancel-room/<str:id>',views.cancel_room,name='cancel-room'),
    path('delete-room/<str:id>',views.delete_room,name='delete-room'),
    path('confirm-now-reserve',views.reserve_confirm(),name="reserve_confirm")

]