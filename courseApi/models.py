from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseId = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.courseId

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='content',null=True,blank=True)
    type = models.CharField(max_length=50, choices=[('video', 'Video'), ('pdf', 'PDF')])
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"
