from rest_framework import serializers
from .models import Course, Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','courseId','type', 'title', 'link']

class CourseSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'courseId', 'title', 'image', 'category', 'content']
