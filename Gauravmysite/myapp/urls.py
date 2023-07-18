
from django.urls import path 
from myapp.views import hello_world, my_hotel_menu
from myapp.views import HelloWorldView, ShowPrinceHobbies

# it maps addresses with their corresponding functions

urlpatterns = [
    # whenever someone is trying to access this address
    # return them the response generated by the 'hello_world' function
    path('hello/', hello_world),
    path('mymenu/', my_hotel_menu),
    path('classhello/', HelloWorldView.as_view()),
    path('hobbies/', ShowPrinceHobbies.as_view())
]