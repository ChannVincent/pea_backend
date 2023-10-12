from core.models.business import Business, YearlyReport, QuarterReport
from integration.models.yahoofinance import YahooFinanceIntegration
from integration.views.yahoofinance import YahooFinanceAPI
import datetime
import json


CASH_MULTIPLIER = 1000000
TIME_BETWEEN_UPDATES = 24 * 30 # hours

def sync():
    integration = YahooFinanceIntegration.objects.first()
    api = YahooFinanceAPI(integration.api_key, integration.api_host)
    businesses = Business.objects.all()
    now = datetime.datetime.now()
    for business in businesses:
        if not business.last_update or business.last_update + datetime.timedelta(hours=TIME_BETWEEN_UPDATES) < now:
            earnings = api.get_earnings(stock=business.symbol, country=business.country_code)
            integrate_earnings(business, earnings)
            cashflow = api.get_cashflow(stock=business.symbol, country=business.country_code)
            integrate_cashflow(business, cashflow)
            business.last_update = now
            business.save()


def integrate_cashflow(business, cashflow):
    time_series = cashflow.get("timeSeries")
    if not time_series:
        pass
    # annual_start_cash_position
    annual_start_cash_position = time_series.get("annualBeginningCashPosition")
    for position in annual_start_cash_position:
        composed_date = position.get("asOfDate")
        if not composed_date:
            continue
        date = composed_date.split("-")[0]
        yearly_report = YearlyReport.objects.filter(business=business, year=date).first()
        if not yearly_report:
            yearly_report = YearlyReport(business=business, year=date)
        yearly_report.start_cash_position = position.get("reportedValue").get("raw") / CASH_MULTIPLIER
        # annual_end_cash_position
        annual_end_cash_position = time_series.get("annualEndCashPosition")
        end_cash_position = [cash for cash in annual_end_cash_position if cash and cash["asOfDate"].startswith(date)]
        yearly_report.end_cash_position = end_cash_position[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if end_cash_position else None
        # annual_debt_repayment
        annual_debt_repayment = time_series.get("annualRepaymentOfDebt")
        debt_repayment = [cash for cash in annual_debt_repayment if cash and cash["asOfDate"].startswith(date)]
        yearly_report.debt_repayment = debt_repayment[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if debt_repayment else None
        # annual_sale_of_investment
        annual_sale_of_investment = time_series.get("annualSaleOfInvestment")
        sale_of_investment = [cash for cash in annual_sale_of_investment if cash and cash["asOfDate"].startswith(date)]
        yearly_report.sale_of_investment = sale_of_investment[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if sale_of_investment else None
        # annual_capital_expenditure
        annual_capital_expenditure = time_series.get("annualCapitalExpenditure")
        capital_expenditure = [cash for cash in annual_capital_expenditure if cash and cash["asOfDate"].startswith(date)]
        yearly_report.capital_expenditure = capital_expenditure[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if capital_expenditure else None
        # annual_purchase_of_investment
        annual_purchase_of_investment = time_series.get("annualPurchaseOfInvestment")
        purchase_of_investment = [cash for cash in annual_purchase_of_investment if cash and cash["asOfDate"].startswith(date)]
        yearly_report.purchase_of_investment = purchase_of_investment[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if purchase_of_investment else None
        # annual_stock_based_compensation
        annual_stock_based_compensation = time_series.get("annualStockBasedCompensation")
        stock_based_compensation = [cash for cash in annual_stock_based_compensation if cash and cash["asOfDate"].startswith(date)]
        yearly_report.stock_based_compensation = stock_based_compensation[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if stock_based_compensation else None
        # annual_net_income
        annual_net_income = time_series.get("annualNetIncome")
        net_income = [cash for cash in annual_net_income if cash and cash["asOfDate"].startswith(date)]
        yearly_report.net_income = net_income[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if net_income else None
        # annual_depreciation_and_ammortization
        annual_depreciation_and_ammortization = time_series.get("annualDepreciationAndAmortization")
        depreciation_and_ammortization = [cash for cash in annual_depreciation_and_ammortization if cash and cash["asOfDate"].startswith(date)]
        yearly_report.depreciation_and_ammortization = depreciation_and_ammortization[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if depreciation_and_ammortization else None
        # annual_net_other_financing_charges
        annual_net_other_financing_charges = time_series.get("annualNetOtherFinancingCharges")
        net_other_financing_charges = [cash for cash in annual_net_other_financing_charges if cash and cash["asOfDate"].startswith(date)]
        yearly_report.net_other_financing_charges = net_other_financing_charges[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if net_other_financing_charges else None
        # annual_other_non_cash_items
        annual_other_non_cash_items = time_series.get("annualOtherNonCashItems")
        other_non_cash_items = [cash for cash in annual_other_non_cash_items if cash and cash["asOfDate"].startswith(date)]
        yearly_report.other_non_cash_items = other_non_cash_items[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if other_non_cash_items else None
        # annual_operating_cash_flow
        annual_operating_cash_flow = time_series.get("annualOperatingCashFlow")
        operating_cash_flow = [cash for cash in annual_operating_cash_flow if cash and cash["asOfDate"].startswith(date)]
        yearly_report.operating_cash_flow = operating_cash_flow[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if operating_cash_flow else None
        # annual_investing_cashflow
        annual_investing_cashflow = time_series.get("annualInvestingCashFlow")
        investing_cashflow = [cash for cash in annual_investing_cashflow if cash and cash["asOfDate"].startswith(date)]
        yearly_report.investing_cashflow = investing_cashflow[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if investing_cashflow else None
        # annual_free_cash_flow
        annual_free_cash_flow = time_series.get("annualFreeCashFlow")
        free_cash_flow = [cash for cash in annual_free_cash_flow if cash and cash["asOfDate"].startswith(date)]
        yearly_report.free_cash_flow = free_cash_flow[0].get("reportedValue").get("raw") / CASH_MULTIPLIER if free_cash_flow else None
        yearly_report.save()
    

def integrate_earnings(business, earnings):
    summary = earnings.get("quoteSummary")
    if not summary:
        return
    results = summary.get("result")
    if not results:
        return
    result = results[0]
    earnings = result.get("earnings")
    financials = earnings.get("financialsChart")
    # yearly reports
    yearly = financials.get("yearly")
    for year in yearly:
        date = year.get("date")
        if not date:
            continue
        yearly_report = YearlyReport.objects.filter(business=business, year=date).first()
        if not yearly_report:
            yearly_report = YearlyReport(business=business, year=date)
        yearly_report.earning = year.get("earnings").get("raw") / CASH_MULTIPLIER
        yearly_report.revenue = year.get("revenue").get("raw") / CASH_MULTIPLIER
        yearly_report.save()
    # quarterly reports
    quarterly = financials.get("quarterly")
    for quarter in quarterly:
        composed_date = quarter.get("date")
        if not composed_date:
            continue
        date = composed_date.split('Q')[1]
        quarter = composed_date.split('Q')[0]
        quarter_report = QuarterReport.objects.filter(business=business, year=date, quarter=quarter).first()
        if not quarter_report:
            quarter_report = QuarterReport(business=business, year=date, quarter=quarter)
        quarter_report.earning = year.get("earnings").get("raw") / CASH_MULTIPLIER
        quarter_report.revenue = year.get("revenue").get("raw") / CASH_MULTIPLIER
        quarter_report.save()

        