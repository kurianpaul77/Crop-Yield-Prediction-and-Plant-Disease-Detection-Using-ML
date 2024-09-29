from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_nursery = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
class Farmer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='farmer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    photo=models.ImageField(upload_to="Photo",unique=True)
    Aadhaar_id = models.ImageField(upload_to="images", unique=True)


class Officer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='officer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    office_regno = models.CharField(max_length=25)
    office_location = models.CharField(max_length=25)
    office_name = models.CharField(max_length=25)
    photo=models.ImageField(upload_to="oPhoto",unique=True)
    id_card = models.ImageField(upload_to="oimages", unique=True)

    def __str__(self):
        return self.name

class upload_img(models.Model):
    img_upload=models.ImageField(upload_to='uploads')



class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    Enquiry = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)

class Announcement(models.Model):
    user = models.ForeignKey(Officer, on_delete=models.CASCADE, related_name='announcement')
    content = models.TextField(max_length=1000)