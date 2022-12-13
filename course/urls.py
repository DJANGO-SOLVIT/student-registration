from rest_framework.urls import path
from django.urls import path
from course.views import StudentAPI
urlpatterns = [
    path('',StudentAPI.as_view(),name='students')
]
