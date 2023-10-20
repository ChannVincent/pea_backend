from core.models.business import Business, YearlyReport, BusinessInfo, BusinessRatio
import datetime

# TODO caculate business_ratio for each year
def caculate_business_ratio(business):
    yearly_reports = YearlyReport.objects.filter(business=business).all()
    for report in yearly_reports:
        year = report.year
        if not year:
            continue
        business_ratio = BusinessRatio.objects.filter(business=business, year=year).first()
        if not business_ratio:
            business_ratio = BusinessRatio(business=business, year=year)
        earnings = report.earning
        revenue = report.revenue
        business_info = BusinessInfo.objects.filter(business=business).first()
        market_cap = business_info.market_cap
        business_ratio.market_cap = market_cap
        business_ratio.cash_position = report.end_cash_position
        business_ratio.debt = report.long_term_debt
        business_ratio.earnings = report.earning
        business_ratio.revenue = report.revenue
        business_ratio.operating_cash_flow = report.operating_cash_flow
        business_ratio.depreciation = report.depreciation
        if earnings and revenue:
            business_ratio.net_margin = earnings * 100 / revenue
        if report.long_term_debt and report.earning:
            business_ratio.years_to_repay_debt = report.long_term_debt / report.earning
        if report.end_cash_position and report.earning:
            business_ratio.years_of_cash = report.end_cash_position / report.earning
        business_ratio.save()
