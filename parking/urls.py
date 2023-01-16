from rest_framework.urls import path
from parking.views import *
urlpatterns = [
    path('reg-parking',CarParkingAPI.as_view()),
    path('reg-parking/<int:id>',CarParkingAPI.as_view()),
    path('reg-parking/',CarParkingAPI.as_view()),
]
