# gunpla/models.py
from django.db import models

class Gunpla(models.Model):
    name = models.CharField(max_length=80)
    series = models.CharField(max_length=120)
    grade = models.CharField(max_length=50)
    scale = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
