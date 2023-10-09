from core.models.business import Business, YearlyReport, QuarterReport
from integration.models.yahoofinance import YahooFinanceIntegration
from integration.views.yahoofinance import YahooFinanceAPI
import json


def sync():
    integration = YahooFinanceIntegration.objects.first()
    api = YahooFinanceAPI(integration.api_key, integration.api_host)
    businesses = Business.objects.all()
    for business in businesses:
        earnings = api.get_earnings(stock=business.symbol, country=business.country_code)
        integrate_earnings(business, earnings)
        cashflow = api.get_cashflow(stock=business.symbol, country=business.country_code)
        integrate_cashflow(business, cashflow)

def integrate_cashflow(business, cashflow):
    cashflow.get("")
    # TODO timeSeries.annualEndCashPosition
    # TODO timeSeries.annualRepaymentOfDebt
    # TODO timeSeries.annualSaleOfInvestment
    # TODO timeSeries.annualCapitalExpenditure

    # TODO timeSeries.annualPurchaseOfInvestment
    # TODO timeSeries.annualStockBasedCompensation

    # TODO timeSeries.annualNetIncome
    # TODO timeSeries.annualDepreciationAndAmortization
    # TODO timeSeries.annualNetOtherFinancingCharges
    # TODO timeSeries.annualOtherNonCashItems
    
    # TODO timeSeries.annualOperatingCashFlow
    # TODO timeSeries.annualInvestingCashFlow
    # TODO timeSeries.annualFreeCashFlow
    
def integrate_earnings(business, earnings):
    summary = earnings.get("quoteSummary")
    if not summary:
        pass
    error = summary.get("error")
    if error != "None":
        print(f"error: {error}")
        pass
    results = summary.get("result")
    if not results:
        pass
    result = results[0]
    earnings = result.get("earnings")
    financials = earnings.get("financialsChart")
    # yearly reports
    yearly = financials.get("yearly")
    for year in yearly:
        date = year.get("date")
        if not date:
            pass
        yearly_report = YearlyReport.objects.filter(business=business, year=date).first()
        if not yearly_report:
            yearly_report = YearlyReport(business=business, year=date)
        yearly_report.earning = year.get("earnings").get("raw")
        yearly_report.revenue = year.get("revenue").get("raw")
        yearly_report.save()
    # quarterly reports
    quarterly = financials.get("quarterly")
    for quarter in quarterly:
        composed_date = quarter.get("date")
        if not composed_date:
            pass
        date = composed_date.split('Q')[1]
        quarter = composed_date.split('Q')[0]
        quarter_report = QuarterReport.objects.filter(business=business, year=date, quarter=quarter).first()
        if not quarter_report:
            quarter_report = QuarterReport(business=business, year=date, quarter=quarter)
        quarter_report.earning = year.get("earnings").get("raw")
        quarter_report.revenue = year.get("revenue").get("raw")
        quarter_report.save()

        