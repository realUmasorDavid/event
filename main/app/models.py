from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    organizer = models.TextField()
    image = models.ImageField(upload_to='images/')
    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']