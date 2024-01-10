from django.contrib import admin

# Register your models here.
from .models import Course, Content
admin.site.register(Course)
admin.site.register(Content)
