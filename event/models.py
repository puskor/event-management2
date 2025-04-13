from django.db import models

# Create your models here.
"""
Event:
    ○ Fields: name, description, date, time, location, category (ForeignKey)
● Participant:
    ○ Fields: name, email, and a ManyToMany relationship with Event.
● Category:
    ○ Fields: name and description."""
    

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
class Event(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True,null=True)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField()
    location=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="events")
    
    def __str__(self):
        return self.name
    

    
class Participant(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    event=models.ManyToManyField(Event,related_name="participant")
    
    def __str__(self):
        return self.name
    