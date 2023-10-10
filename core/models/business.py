from django.db import models


class Business(models.Model):
    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=20, unique=True, default="")
    country_code = models.CharField(max_length=20, default="EU")

    def __str__(self):
        return self.name
    

class QuarterReport(models.Model):
    class Meta:
        verbose_name = "Quarter Report"
        verbose_name_plural = "Quarter Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    quarter = models.IntegerField(default=1)
    earning = models.IntegerField(default=None, null=True)
    revenue = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f"{self.business}_{self.year}Q{self.quarter}"


class YearlyReport(models.Model):
    class Meta:
        verbose_name = "Yearly Report"
        verbose_name_plural = "Yearly Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    earning = models.IntegerField(default=None, null=True)
    revenue = models.IntegerField(default=None, null=True)
    start_cash_position = models.IntegerField(default=None, null=True)
    end_cash_position = models.IntegerField(default=None, null=True)
    debt_repayment = models.IntegerField(default=None, null=True)
    sale_of_investment = models.IntegerField(default=None, null=True)
    capital_expenditure = models.IntegerField(default=None, null=True)
    purchase_of_investment = models.IntegerField(default=None, null=True)
    stock_based_compensation = models.IntegerField(default=None, null=True)
    net_income = models.IntegerField(default=None, null=True)
    depreciation_and_ammortization = models.IntegerField(default=None, null=True)
    net_other_financing_charges = models.IntegerField(default=None, null=True)
    other_non_cash_items = models.IntegerField(default=None, null=True)
    operating_cash_flow = models.IntegerField(default=None, null=True)
    investing_cashflow = models.IntegerField(default=None, null=True)
    free_cash_flow = models.IntegerField(default=None, null=True)
    
    def __str__(self):
        return f"{self.business}_{self.year}"