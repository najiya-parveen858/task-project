from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student (models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    dept=models.CharField(max_length=100)
    year=models.IntegerField()
    photo=models.ImageField(upload_to="student_photo/")

    def str(self):
        return self.name