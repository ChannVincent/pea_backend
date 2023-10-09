from django.db import models

class YahooFinanceIntegration(models.Model):
    api_key = models.CharField(max_length=256)
    api_host = models.CharField(max_length=256)
    