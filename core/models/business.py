from django.db import models

class Business(models.Model):
    Name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=20, unique=True, default="")