from django.db import models


class Business(models.Model):
    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"
    COUNTRY_CHOICES = (
        ("FR", "France"),("DE", "Germany"),("ES", "Spain"),
        ("CH", "Switzerland"),("UK", "United Kingdom"),("PT", "Portugal"),
        ("BE", "Belgium"),("EL", "Greece"),("IE", "Ireland"),
        ("LU", "Luxembourg"),("FI", "Finland"),("IT", "Italy"),
        ("LI", "Liechtenstein"),("IS", "Iceland"),("NO", "Norway"),
        ("SE", "Sweden"),("LT", "Lithuania"),("BG", "Bulgaria"),
        ("CZ", "Czechia"),("HU", "Hungary"),("RO", "Romania"),
        ("SI", "Slovenia"),("DK", "Denmark"),("HR", "Croatia"),
        ("MT", "Malta"),("SK", "Slovakia"),("NL", "Netherlands"),
        ("EE", "Estonia"),("CY", "Cyprus"),("AT", "Austria"),
        ("LV", "Latvia"),("PL", "Poland"),
    )
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=20, unique=True, default="")
    country_code = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default="FR")
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'symbol': self.symbol,
            'country_code': self.country_code,
        }
    

class QuarterReport(models.Model):
    class Meta:
        verbose_name = "Quarter Report"
        verbose_name_plural = "Quarter Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    quarter = models.IntegerField(default=1)
    earning = models.IntegerField(default=None, null=True, blank=True)
    revenue = models.IntegerField(default=None, null=True, blank=True)
    # balance sheet
    cash = models.IntegerField(default=None, null=True, blank=True)
    inventory = models.IntegerField(default=None, null=True, blank=True)
    total_assets = models.IntegerField(default=None, null=True, blank=True)
    total_current_assets = models.IntegerField(default=None, null=True, blank=True)
    treasury_stock = models.IntegerField(default=None, null=True, blank=True)
    intangible_assets = models.IntegerField(default=None, null=True, blank=True)
    net_tangible_assets = models.IntegerField(default=None, null=True, blank=True)
    total_current_liabilities = models.IntegerField(default=None, null=True, blank=True)
    short_long_term_debt = models.IntegerField(default=None, null=True, blank=True)
    long_term_debt = models.IntegerField(default=None, null=True, blank=True)
    long_term_investments = models.IntegerField(default=None, null=True, blank=True)
    short_term_investments = models.IntegerField(default=None, null=True, blank=True)
    # cashflow
    net_income = models.IntegerField(default=None, null=True, blank=True) 
    investments = models.IntegerField(default=None, null=True, blank=True) 
    change_in_cash = models.IntegerField(default=None, null=True, blank=True) 
    depreciation = models.IntegerField(default=None, null=True, blank=True) 
    dividends_paid = models.IntegerField(default=None, null=True, blank=True) 
    net_borrowings = models.IntegerField(default=None, null=True, blank=True) 
    change_to_inventory = models.IntegerField(default=None, null=True, blank=True) 
    change_to_netincome = models.IntegerField(default=None, null=True, blank=True) 
    repurchase_of_stock = models.IntegerField(default=None, null=True, blank=True) 
    capital_expenditures = models.IntegerField(default=None, null=True, blank=True) 
    change_to_liabilities = models.IntegerField(default=None, null=True, blank=True) 
    effect_of_exchange_rate = models.IntegerField(default=None, null=True, blank=True) 
    change_to_account_receivables = models.IntegerField(default=None, null=True, blank=True) 
    change_tooperating_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cash_from_financing_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cash_from_operating_activities = models.IntegerField(default=None, null=True, blank=True) 
    other_cashflows_from_financing_activities = models.IntegerField(default=None, null=True, blank=True) 
    other_cashflows_from_investing_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cashflows_from_investing_activities = models.IntegerField(default=None, null=True, blank=True) 
    
    def __str__(self):
        return f"{self.business}_{self.year}Q{self.quarter}"

    def serialize(self):
        return {
            'year': self.year,
            'quarter': self.quarter,
            'earning': self.earning,
            'revenue': self.revenue,
        }
    

class YearlyReport(models.Model):
    class Meta:
        verbose_name = "Yearly Report"
        verbose_name_plural = "Yearly Reports"
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(default=1970)
    earning = models.IntegerField(default=None, null=True, blank=True)
    revenue = models.IntegerField(default=None, null=True, blank=True)
    # time_series
    start_cash_position = models.IntegerField(default=None, null=True, blank=True)
    end_cash_position = models.IntegerField(default=None, null=True, blank=True)
    debt_repayment = models.IntegerField(default=None, null=True, blank=True)
    sale_of_investment = models.IntegerField(default=None, null=True, blank=True)
    capital_expenditure = models.IntegerField(default=None, null=True, blank=True)
    purchase_of_investment = models.IntegerField(default=None, null=True, blank=True)
    stock_based_compensation = models.IntegerField(default=None, null=True, blank=True)
    depreciation_and_ammortization = models.IntegerField(default=None, null=True, blank=True)
    net_other_financing_charges = models.IntegerField(default=None, null=True, blank=True)
    other_non_cash_items = models.IntegerField(default=None, null=True, blank=True)
    operating_cash_flow = models.IntegerField(default=None, null=True, blank=True)
    investing_cashflow = models.IntegerField(default=None, null=True, blank=True)
    free_cash_flow = models.IntegerField(default=None, null=True, blank=True)
    # balance sheet
    cash = models.IntegerField(default=None, null=True, blank=True)
    inventory = models.IntegerField(default=None, null=True, blank=True)
    total_assets = models.IntegerField(default=None, null=True, blank=True)
    total_current_assets = models.IntegerField(default=None, null=True, blank=True)
    treasury_stock = models.IntegerField(default=None, null=True, blank=True)
    intangible_assets = models.IntegerField(default=None, null=True, blank=True)
    net_tangible_assets = models.IntegerField(default=None, null=True, blank=True)
    total_current_liabilities = models.IntegerField(default=None, null=True, blank=True)
    short_long_term_debt = models.IntegerField(default=None, null=True, blank=True)
    long_term_debt = models.IntegerField(default=None, null=True, blank=True)
    long_term_investments = models.IntegerField(default=None, null=True, blank=True)
    short_term_investments = models.IntegerField(default=None, null=True, blank=True)
    # cashflow
    net_income = models.IntegerField(default=None, null=True, blank=True) 
    investments = models.IntegerField(default=None, null=True, blank=True) 
    change_in_cash = models.IntegerField(default=None, null=True, blank=True) 
    depreciation = models.IntegerField(default=None, null=True, blank=True) 
    dividends_paid = models.IntegerField(default=None, null=True, blank=True) 
    net_borrowings = models.IntegerField(default=None, null=True, blank=True) 
    change_to_inventory = models.IntegerField(default=None, null=True, blank=True) 
    change_to_netincome = models.IntegerField(default=None, null=True, blank=True) 
    repurchase_of_stock = models.IntegerField(default=None, null=True, blank=True) 
    capital_expenditures = models.IntegerField(default=None, null=True, blank=True) 
    change_to_liabilities = models.IntegerField(default=None, null=True, blank=True) 
    effect_of_exchange_rate = models.IntegerField(default=None, null=True, blank=True) 
    change_to_account_receivables = models.IntegerField(default=None, null=True, blank=True) 
    change_tooperating_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cash_from_financing_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cash_from_operating_activities = models.IntegerField(default=None, null=True, blank=True) 
    other_cashflows_from_financing_activities = models.IntegerField(default=None, null=True, blank=True) 
    other_cashflows_from_investing_activities = models.IntegerField(default=None, null=True, blank=True) 
    total_cashflows_from_investing_activities = models.IntegerField(default=None, null=True, blank=True) 

    def __str__(self):
        return f"{self.business}_{self.year}"
    
    def serialize(self):
        return {
            'year': self.year,
            'earning': self.earning,
            'revenue': self.revenue,
            'start_cash_position': self.start_cash_position,
            'end_cash_position': self.end_cash_position,
            'debt_repayment': self.debt_repayment,
            'sale_of_investment': self.sale_of_investment,
            'capital_expenditure': self.capital_expenditure,
            'purchase_of_investment': self.purchase_of_investment,
            'stock_based_compensation': self.stock_based_compensation,
            'net_income': self.net_income,
            'depreciation_and_ammortization': self.depreciation_and_ammortization,
            'net_other_financing_charges': self.net_other_financing_charges,
            'other_non_cash_items': self.other_non_cash_items,
            'operating_cash_flow': self.operating_cash_flow,
            'investing_cashflow': self.investing_cashflow,
            'free_cash_flow': self.free_cash_flow,
        }