from core.models.business import Business, BusinessEvent, BusinessInfo, Industry, Sector, YearlyReport, QuarterReport, AnalystGrade, GradeFirm, MarketPrice
from integration.models.yahoofinance import YahooFinanceIntegration
from integration.views.yahoofinance import YahooFinanceAPI
import datetime
import json


CASH_MULTIPLIER = 1 * 1000 * 1000 # 1M
TIME_BETWEEN_UPDATES = 24 * 30 # hours

def sync(force=False):
    integration = YahooFinanceIntegration.objects.first()
    api = YahooFinanceAPI(integration.api_key, integration.api_host)
    businesses = Business.objects.all()
    now = datetime.datetime.now()
    for business in businesses:
        if not business.last_update or business.last_update + datetime.timedelta(hours=TIME_BETWEEN_UPDATES) < now or force:
            cashflow = api.get_cashflow(stock=business.symbol, country=business.country_code)
            integrate_cashflow(business, cashflow)
            summary = api.get_summary(stock=business.symbol, country=business.country_code)
            integrate_summary(business, summary)
            # recent_updates = api.get_updates(stock=business.symbol, country=business.country_code)
            # integrate_recent_updates(business, recent_updates)
            market_price = api.get_market_price(stock=business.symbol, country=business.country_code)
            integrate_market_price(business, market_price)
            business.last_update = now
            business.save()


def integrate_cashflow(business, cashflow):
    time_series = cashflow.get("timeSeries")
    if not time_series:
        return
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
    # earnings
    earnings = cashflow.get("earnings")
    financials_chart = earnings.get("financialsChart")
    if not financials_chart:
        return
    # quarterly reports
    quarterly = financials_chart.get("quarterly")
    for quarter in quarterly:
        composed_date = quarter.get("date")
        if not composed_date:
            continue
        date = composed_date.split('Q')[1]
        dquarter = composed_date.split('Q')[0]
        quarter_report = QuarterReport.objects.filter(business=business, year=date, quarter=dquarter).first()
        if not quarter_report:
            quarter_report = QuarterReport(business=business, year=date, quarter=dquarter)
        quarter_report.earning = quarter.get("earnings").get("raw") / CASH_MULTIPLIER
        quarter_report.revenue = quarter.get("revenue").get("raw") / CASH_MULTIPLIER
        if quarter_report.earning == 0 and quarter_report.revenue == 0:
            continue
        quarter_report.save()
    # yearly earnings & revenue
    yearly = financials_chart.get("yearly")
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
    # yearly balance sheet
    balance_sheets_history = cashflow.get("balanceSheetHistory")
    if not balance_sheets_history:
        return
    balance_sheets = balance_sheets_history.get("balanceSheetStatements")
    for balance in balance_sheets:
        endDate = balance.get("endDate").get("fmt")
        if not endDate:
            continue
        date = endDate.split("-")[0]
        yearly_report = YearlyReport.objects.filter(business=business, year=date).first()
        if not yearly_report:
            yearly_report = YearlyReport(business=business, year=date)
        yearly_report.cash = balance.get("cash").get("raw") / CASH_MULTIPLIER if balance.get("cash") else None
        yearly_report.inventory = balance.get("inventory").get("raw") / CASH_MULTIPLIER if balance.get("inventory") else None
        yearly_report.total_assets = balance.get("totalAssets").get("raw") / CASH_MULTIPLIER if balance.get("totalAssets") else None
        yearly_report.total_current_assets = balance.get("totalCurrentAssets").get("raw") / CASH_MULTIPLIER if balance.get("totalCurrentAssets") else None
        yearly_report.treasury_stock = balance.get("treasuryStock").get("raw") / CASH_MULTIPLIER if balance.get("treasuryStock") else None
        yearly_report.intangible_assets = balance.get("intangibleAssets").get("raw") / CASH_MULTIPLIER if balance.get("intangibleAssets") else None
        yearly_report.net_tangible_assets = balance.get("netTangibleAssets").get("raw") / CASH_MULTIPLIER if balance.get("netTangibleAssets") else None
        yearly_report.total_current_liabilities = balance.get("totalCurrentLiabilities").get("raw") / CASH_MULTIPLIER if balance.get("totalCurrentLiabilities") else None
        yearly_report.short_long_term_debt = balance.get("shortLongTermDebt").get("raw") / CASH_MULTIPLIER if balance.get("shortLongTermDebt") else None
        yearly_report.long_term_debt = balance.get("longTermDebt").get("raw") / CASH_MULTIPLIER if balance.get("longTermDebt") else None
        yearly_report.long_term_investments = balance.get("longTermInvestments").get("raw") / CASH_MULTIPLIER if balance.get("longTermInvestments") else None
        yearly_report.short_term_investments = balance.get("shortTermInvestments").get("raw") / CASH_MULTIPLIER if balance.get("shortTermInvestments") else None
        yearly_report.save()
    # quarter balance sheet
    quarter_balance_sheets_history = cashflow.get("balanceSheetHistoryQuarterly")
    if not quarter_balance_sheets_history:
        return
    quarter_balance_sheets = quarter_balance_sheets_history.get("balanceSheetStatements")
    for balance in quarter_balance_sheets:
        endDate = balance.get("endDate").get("fmt")
        if not endDate:
            continue
        date = endDate.split("-")[0]
        month = int(endDate.split("-")[1])
        quarter = 0
        if month in [2,3,4]:
            quarter = 1
        if month in [5,6,7]:
            quarter = 2
        if month in [8,9,10]:
            quarter = 3
        if month in [11, 12, 1]:
            quarter = 4
        quarter_report = QuarterReport.objects.filter(business=business, year=date, quarter=quarter).first()
        if not quarter_report:
            quarter_report = QuarterReport(business=business, year=date, quarter=quarter)
        quarter_report.cash = balance.get("cash").get("raw") / CASH_MULTIPLIER if balance.get("cash") else None
        quarter_report.inventory = balance.get("inventory").get("raw") / CASH_MULTIPLIER if balance.get("inventory") else None
        quarter_report.total_assets = balance.get("totalAssets").get("raw") / CASH_MULTIPLIER if balance.get("totalAssets") else None
        quarter_report.total_current_assets = balance.get("totalCurrentAssets").get("raw") / CASH_MULTIPLIER if balance.get("totalCurrentAssets") else None
        quarter_report.treasury_stock = balance.get("treasuryStock").get("raw") / CASH_MULTIPLIER if balance.get("treasuryStock") else None
        quarter_report.intangible_assets = balance.get("intangibleAssets").get("raw") / CASH_MULTIPLIER if balance.get("intangibleAssets") else None
        quarter_report.net_tangible_assets = balance.get("netTangibleAssets").get("raw") / CASH_MULTIPLIER if balance.get("netTangibleAssets") else None
        quarter_report.total_current_liabilities = balance.get("totalCurrentLiabilities").get("raw") / CASH_MULTIPLIER if balance.get("totalCurrentLiabilities") else None
        quarter_report.short_long_term_debt = balance.get("shortLongTermDebt").get("raw") / CASH_MULTIPLIER if balance.get("shortLongTermDebt") else None
        quarter_report.long_term_debt = balance.get("longTermDebt").get("raw") / CASH_MULTIPLIER if balance.get("longTermDebt") else None
        quarter_report.long_term_investments = balance.get("longTermInvestments").get("raw") / CASH_MULTIPLIER if balance.get("longTermInvestments") else None
        quarter_report.short_term_investments = balance.get("shortTermInvestments").get("raw") / CASH_MULTIPLIER if balance.get("shortTermInvestments") else None
        quarter_report.save()
    # yearly cashflow
    cashflow_history = cashflow.get("cashflowStatementHistory")
    if not cashflow_history:
        return
    yearly_cashflow = cashflow_history.get("cashflowStatements")
    for year in yearly_cashflow:
        endDate = year.get("endDate").get("fmt")
        if not endDate:
            continue
        date = endDate.split("-")[0]
        yearly_report = YearlyReport.objects.filter(business=business, year=date).first()
        if not yearly_report:
            yearly_report = YearlyReport(business=business, year=date)
        yearly_report.net_income = year.get("netIncome").get("raw") / CASH_MULTIPLIER if year.get("netIncome") else None
        yearly_report.investments = year.get("investments").get("raw") / CASH_MULTIPLIER if year.get("investments") else None
        yearly_report.change_in_cash = year.get("changeInCash").get("raw") / CASH_MULTIPLIER if year.get("changeInCash") else None
        yearly_report.depreciation = year.get("depreciation").get("raw") / CASH_MULTIPLIER if year.get("depreciation") else None
        yearly_report.dividends_paid = year.get("dividendsPaid").get("raw") / CASH_MULTIPLIER if year.get("dividendsPaid") else None
        yearly_report.net_borrowings = year.get("netBorrowings").get("raw") / CASH_MULTIPLIER if year.get("netBorrowings") else None
        yearly_report.change_to_inventory = year.get("changeToInventory").get("raw") / CASH_MULTIPLIER if year.get("changeToInventory") else None
        yearly_report.change_to_netincome = year.get("changeToNetincome").get("raw") / CASH_MULTIPLIER if year.get("changeToNetincome") else None
        yearly_report.repurchase_of_stock = year.get("repurchaseOfStock").get("raw") / CASH_MULTIPLIER if year.get("repurchaseOfStock") else None
        yearly_report.capital_expenditures = year.get("capitalExpenditures").get("raw") / CASH_MULTIPLIER if year.get("capitalExpenditures") else None
        yearly_report.change_to_liabilities = year.get("changeToLiabilities").get("raw") / CASH_MULTIPLIER if year.get("changeToLiabilities") else None
        yearly_report.effect_of_exchange_rate = year.get("effectOfExchangeRate").get("raw") / CASH_MULTIPLIER if year.get("effectOfExchangeRate") else None
        yearly_report.change_to_account_receivables = year.get("changeToAccountReceivables").get("raw") / CASH_MULTIPLIER if year.get("changeToAccountReceivables") else None
        yearly_report.change_tooperating_activities = year.get("changeToOperatingActivities").get("raw") / CASH_MULTIPLIER if year.get("changeToOperatingActivities") else None
        yearly_report.total_cash_from_financing_activities = year.get("totalCashFromFinancingActivities").get("raw") / CASH_MULTIPLIER if year.get("totalCashFromFinancingActivities") else None
        yearly_report.total_cash_from_operating_activities = year.get("totalCashFromOperatingActivities").get("raw") / CASH_MULTIPLIER if year.get("totalCashFromOperatingActivities") else None
        yearly_report.other_cashflows_from_financing_activities = year.get("otherCashflowsFromFinancingActivities").get("raw") / CASH_MULTIPLIER if year.get("otherCashflowsFromFinancingActivities") else None
        yearly_report.other_cashflows_from_investing_activities = year.get("otherCashflowsFromInvestingActivities").get("raw") / CASH_MULTIPLIER if year.get("otherCashflowsFromInvestingActivities") else None
        yearly_report.total_cashflows_from_investing_activities = year.get("totalCashflowsFromInvestingActivities").get("raw") / CASH_MULTIPLIER if year.get("totalCashflowsFromInvestingActivities") else None
        yearly_report.save()
    # quarterly cashflow
    quarter_cashflow_history = cashflow.get("cashflowStatementHistoryQuarterly")
    if not quarter_cashflow_history:
        return
    quarter_cashflow = quarter_cashflow_history.get("cashflowStatements")
    for quarter in quarter_cashflow:
        endDate = quarter.get("endDate").get("fmt")
        if not endDate:
            continue
        date = endDate.split("-")[0]
        month = int(endDate.split("-")[1])
        dquarter = 0
        if month in [2,3,4]:
            dquarter = 1
        if month in [5,6,7]:
            dquarter = 2
        if month in [8,9,10]:
            dquarter = 3
        if month in [11,12,1]:
            dquarter = 4
        quarter_report = QuarterReport.objects.filter(business=business, year=date, quarter=dquarter).first()
        if not quarter_report:
            quarter_report = QuarterReport(business=business, year=date, quarter=quarter)
        quarter_report.net_income = quarter.get("netIncome").get("raw") / CASH_MULTIPLIER if quarter.get("netIncome") else None
        quarter_report.investments = quarter.get("investments").get("raw") / CASH_MULTIPLIER if quarter.get("investments") else None
        quarter_report.change_in_cash = quarter.get("changeInCash").get("raw") / CASH_MULTIPLIER if quarter.get("changeInCash") else None
        quarter_report.depreciation = quarter.get("depreciation").get("raw") / CASH_MULTIPLIER if quarter.get("depreciation") else None
        quarter_report.dividends_paid = quarter.get("dividendsPaid").get("raw") / CASH_MULTIPLIER if quarter.get("dividendsPaid") else None
        quarter_report.net_borrowings = quarter.get("netBorrowings").get("raw") / CASH_MULTIPLIER if quarter.get("netBorrowings") else None
        quarter_report.change_to_inventory = quarter.get("changeToInventory").get("raw") / CASH_MULTIPLIER if quarter.get("changeToInventory") else None
        quarter_report.change_to_netincome = quarter.get("changeToNetincome").get("raw") / CASH_MULTIPLIER if quarter.get("changeToNetincome") else None
        quarter_report.repurchase_of_stock = quarter.get("repurchaseOfStock").get("raw") / CASH_MULTIPLIER if quarter.get("repurchaseOfStock") else None
        quarter_report.capital_expenditures = quarter.get("capitalExpenditures").get("raw") / CASH_MULTIPLIER if quarter.get("capitalExpenditures") else None
        quarter_report.change_to_liabilities = quarter.get("changeToLiabilities").get("raw") / CASH_MULTIPLIER if quarter.get("changeToLiabilities") else None
        quarter_report.effect_of_exchange_rate = quarter.get("effectOfExchangeRate").get("raw") / CASH_MULTIPLIER if quarter.get("effectOfExchangeRate") else None
        quarter_report.change_to_account_receivables = quarter.get("changeToAccountReceivables").get("raw") / CASH_MULTIPLIER if quarter.get("changeToAccountReceivables") else None
        quarter_report.change_tooperating_activities = quarter.get("changeToOperatingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("changeToOperatingActivities") else None
        quarter_report.total_cash_from_financing_activities = quarter.get("totalCashFromFinancingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("totalCashFromFinancingActivities") else None
        quarter_report.total_cash_from_operating_activities = quarter.get("totalCashFromOperatingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("totalCashFromOperatingActivities") else None
        quarter_report.other_cashflows_from_financing_activities = quarter.get("otherCashflowsFromFinancingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("otherCashflowsFromFinancingActivities") else None
        quarter_report.other_cashflows_from_investing_activities = quarter.get("otherCashflowsFromInvestingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("otherCashflowsFromInvestingActivities") else None
        quarter_report.total_cashflows_from_investing_activities = quarter.get("totalCashflowsFromInvestingActivities").get("raw") / CASH_MULTIPLIER if quarter.get("totalCashflowsFromInvestingActivities") else None
        quarter_report.save()


def integrate_summary(business, summary):
    profile = summary.get("summaryProfile")
    business_info = BusinessInfo.objects.filter(business=business).last()
    if not business_info:
        business_info = BusinessInfo(business=business)
    business_info.long_business_summary = profile.get("longBusinessSummary")
    business_info.website = profile.get("website")
    business_info.country = profile.get("country")
    business_info.city = profile.get("city")
    business_info.full_time_employees = profile.get("fullTimeEmployees")
    price = summary.get("price")
    if price:
        business_info.market_cap = price.get("marketCap").get("raw") / CASH_MULTIPLIER if price.get("marketCap") else None
    # industry
    industry_key = profile.get("industryKey")
    if not industry_key:
        return
    industry = Industry.objects.filter(industry_key=industry_key).first()
    if not industry:
        industry = Industry(industry_key=industry_key)
    industry.industry = profile.get("industryDisp")
    industry.save()
    business_info.industry = industry
    # sector
    sector_key = profile.get("sectorKey")
    if not sector_key:
        return
    sector = Sector.objects.filter(sector_key=sector_key).first()
    if not sector:
        sector = Sector(sector_key=sector_key)
    sector.sector_disp = profile.get("sectorDisp")
    sector.sector = profile.get("sector")
    sector.save()
    business_info.sector = sector
    business_info.save()
    # upgrade downgrade : nothing for french industry ?
    upgrade_downgrade_history = summary.get("upgradeDowngradeHistory")
    if not upgrade_downgrade_history:
        return
    grade_history = upgrade_downgrade_history.get("history")
    business_info = BusinessInfo.objects.filter(business=business).first()
    if not business_info:
        return
    for grade in grade_history:
        timestamp = grade.get("epochGradeDate")
        if not timestamp:
            continue
        date = datetime.datetime.fromtimestamp(timestamp)
        analyst_grade = AnalystGrade.objects.filter(date=date, business_info=business_info)
        if not analyst_grade:
            analyst_grade = AnalystGrade(date=date, business_info=business_info)
        grade_firm = GradeFirm.objects.filter(name=grade.get("firm"))
        if not grade_firm:
            grade_firm = GradeFirm(name=grade.get("firm"))
        analyst_grade.firm = grade_firm
        analyst_grade.fromGrade = grade.get("fromGrade")
        analyst_grade.toGrade = grade.get("toGrade")
        analyst_grade.action = grade.get("action")
        analyst_grade.save()


def integrate_recent_updates(business, recent_updates):
    summary = recent_updates.get("quoteSummary")
    if not summary:
        return
    result = summary.get("result")
    if not result:
        return
    # grades
    upgrade_downgrade_history = result[0].get("upgradeDowngradeHistory")
    if not upgrade_downgrade_history:
        return
    grade_history = upgrade_downgrade_history.get("history")
    business_info = BusinessInfo.objects.filter(business=business).first()
    if not business_info:
        return
    for grade in grade_history:
        timestamp = grade.get("epochGradeDate")
        if not timestamp:
            continue
        date = datetime.datetime.fromtimestamp(timestamp)
        analyst_grade = AnalystGrade.objects.filter(date=date, business_info=business_info)
        if not analyst_grade:
            analyst_grade = AnalystGrade(date=date, business_info=business_info)
        grade_firm = GradeFirm.objects.filter(name=grade.get("firm"))
        if not grade_firm:
            grade_firm = GradeFirm(name=grade.get("firm"))
        analyst_grade.firm = grade_firm
        analyst_grade.fromGrade = grade.get("fromGrade")
        analyst_grade.toGrade = grade.get("toGrade")
        analyst_grade.action = grade.get("action")
        analyst_grade.save()
        

def integrate_market_price(business, market_price_data):
    prices = market_price_data.get("prices")
    if not prices:
        return
    for price in prices:
        timestamp = price.get("date")
        if not timestamp:
            continue
        date = datetime.datetime.fromtimestamp(timestamp)
        market_price = MarketPrice.objects.filter(business=business, date=date).first()
        if not market_price:
            market_price = MarketPrice(business=business, date=date)
        market_price.open = price.get("open")
        market_price.high = price.get("high")
        market_price.low = price.get("low")
        market_price.close = price.get("close")
        market_price.volume = price.get("volume")
        market_price.adjclose = price.get("adjclose")
        market_price.save()
    events = market_price_data.get("eventsData")
    for event in events:
        timestamp = event.get("date")
        if not timestamp:
            continue
        date = datetime.datetime.fromtimestamp(timestamp)
        business_event = BusinessEvent.objects.filter(business=business, date=date)
        if not business_event:
            business_event = BusinessEvent(business=business, date=date)
        business_event.type = event.get("type")
        business_event.amount = event.get("amount")
        business_event.data = event.get("data")
        business_event.save()
