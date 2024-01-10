# urls.py
from django.urls import path, include
from .views import ContentViewSet, CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('courses', CourseViewSet, basename='course')
router.register('content', ContentViewSet, basename='content')

urlpatterns = [
   path('', include(router.urls))
]
