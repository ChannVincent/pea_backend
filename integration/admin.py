from django.contrib import admin
from .models import AlphavantageIntegration
from .models import YahooFinanceIntegration

admin.site.register(AlphavantageIntegration)
admin.site.register(YahooFinanceIntegration)
