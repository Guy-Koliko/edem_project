from django.db import models
from django.utils import timezone

# Create your models here.
class Realtor(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  email = models.EmailField()
  phone = models.CharField(max_length=100)
  is_mvp = models.BooleanField(default=True)
  hire_date = models.DateTimeField(default=timezone.now,blank=True)
  photo = models.ImageField(upload_to='upload/%Y/%m/%d/',blank=True)
  
  def __str__(self):
    return self.name