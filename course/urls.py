from rest_framework.urls import path
from django.urls import path
from course.views import StudentAPI,CourseAPI
urlpatterns = [
    path('',CourseAPI.as_view(),name='course'),
]
