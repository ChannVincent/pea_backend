from core.models.business import Business, YearlyReport, BusinessInfo, BusinessRatio
import datetime

def caculate_business_ratio(business):
    business_ratio = BusinessRatio.objects.filter(business=business).first()
    if not business_ratio:
        business_ratio = BusinessRatio(business=business)
    last_year = datetime.datetime.now().year - 1
    last_yearly_report = YearlyReport.objects.filter(business=business, year=last_year).first()
    earnings = last_yearly_report.earning
    revenue = last_yearly_report.revenue
    business_info = BusinessInfo.objects.filter(business=business).first()
    market_cap = business_info.market_cap
    # def
    business_ratio.market_cap = market_cap
    business_ratio.net_margin = earnings / revenue
    business_ratio.cash_position = last_yearly_report.end_cash_position
    business_ratio.debt = last_yearly_report.long_term_debt
    business_ratio.earnings = last_yearly_report.earning
    business_ratio.revenue = last_yearly_report.revenue
    business_ratio.save()
