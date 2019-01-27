from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    description = models.TextField()
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
