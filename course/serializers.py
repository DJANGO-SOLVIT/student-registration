from rest_framework import serializers
from course.models import CourseStudents, Course
from django.utils import timezone


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


    def validate_course_code(self, value):
        if Course.objects.filter(course_code=value).exists():
            raise serializers.ValidationError(
                "Course with coede already  exist")
        else:
            return value
        # try:
        #     Course.objects.get(course_code=value)
        #     raise serializers.ValidationError("something")
        # except Course.DoesNotExist:
        #     return value


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
