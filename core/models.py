from django.db import models


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guest_number = models.IntegerField()
    mobile = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

    class Meta:
        ordering = ["-date", "-time"]
