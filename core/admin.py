from django.contrib import admin
from .models.business import Business, BusinessInfo, AnalystGrade, Industry, Sector, QuarterReport, YearlyReport, MarketPrice, BusinessEvent


class YearlyReportInline(admin.TabularInline):
    model = YearlyReport
    extra = 0

class AnalystGradeInline(admin.TabularInline):
    model = AnalystGrade
    extra = 0
    
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

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol")
    inlines = [YearlyReportInline]

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ("business", "last_update")
    inlines = [AnalystGradeInline]

@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_filter = ("business",)

@admin.register(BusinessEvent)
class BusinessEventAdmin(admin.ModelAdmin):
    list_filter = ("business",)
    