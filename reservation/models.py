from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.CharField(max_length=31)
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Room - {self.number}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booking")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room} booked - by {self.user}"
