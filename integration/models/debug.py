from django.db import models

class DebugApiLog(models.Model):
    date = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=256)
    data = models.JSONField(blank=True, null=True)
    params = models.JSONField(blank=True, null=True)