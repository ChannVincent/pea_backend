from django.contrib import admin
from .models.business import Business, QuarterReport, YearlyReport

admin.site.register(Business)
admin.site.register(QuarterReport)
admin.site.register(YearlyReport)
