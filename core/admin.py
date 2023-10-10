from django.contrib import admin
from .models.business import Business, QuarterReport, YearlyReport


@admin.register(QuarterReport)
class QuarterReportAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ("business", "year", "quarter")
    list_filter = ("business",)

@admin.register(YearlyReport)
class YearlyReportAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ("business", "year")
    list_filter = ("business",)

class YearlyReportInline(admin.TabularInline):
    model = YearlyReport
    extra = 0

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol")
    inlines = [YearlyReportInline]
