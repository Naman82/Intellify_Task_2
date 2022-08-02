from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to = 'student/profile')
    registration_id = models.CharField(max_length=10,blank=True,unique=True)
    standard = models.CharField(max_length=10,blank=True)
    class_section = models.CharField(max_length=10,blank=True)
    stream = models.CharField(max_length=50,blank=True)
    roll_number = models.IntegerField()

class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to = 'teacher/profile')
    teacher_id = models.CharField(max_length=10,blank=True,unique=True)
    subject = models.CharField(max_length=255,blank=True)
    class_taught = models.CharField(max_length=255,blank=True)
    contact_number = models.IntegerField()

