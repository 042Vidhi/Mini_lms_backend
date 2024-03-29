# Generated by Django 4.2.7 on 2024-01-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.ManyToManyField(to='courseApi.content'),
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('video', 'Video'), ('pdf', 'PDF')], max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
