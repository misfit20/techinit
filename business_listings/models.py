from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.name}, {self.description}"