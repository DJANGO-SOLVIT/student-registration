from rest_framework import serializers
from course.models import CourseStudents, Course
from django.utils import timezone


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseStudentsSerializer(serializers.ModelSerializer):
    current_time = serializers.DateTimeField(default=timezone.now())

    class Meta:
        model = CourseStudents
        fields = [
            'id',
            'course',
            'students',
            'current_time'
        ]
