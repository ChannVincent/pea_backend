from django.contrib import admin
from .models import AlphavantageIntegration
from .models import YahooFinanceIntegration
from .models import DebugApiLog


admin.site.register(AlphavantageIntegration)
admin.site.register(YahooFinanceIntegration)

@admin.register(DebugApiLog)
class DebugApiLogAdmin(admin.ModelAdmin):
    list_display = ("date", "url", "params")