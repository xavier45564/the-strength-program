from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    dxCode = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(blank=True, default=None)
    subject = models.CharField(max_length=200)
    agency = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=200)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.email