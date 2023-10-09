from django.db import models

class AlphavantageIntegration(models.Model):
    api_key = models.CharField(max_length=256)
    base_url = models.CharField(max_length=256, default="")
    