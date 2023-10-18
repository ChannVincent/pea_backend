from django.shortcuts import render
from core.models.business import Business, YearlyReport, QuarterReport
from django.http import JsonResponse


def get_business_detail(request, business_pk):
    if not business_pk:
        return JsonResponse({'status': 'error : no business found'})
    years = []
    yearly_reports = YearlyReport.objects.filter(business__pk=business_pk)
    for year in yearly_reports:
        years.append(year.serialize())
    quarters = []
    quarter_reports = QuarterReport.objects.filter(business__pk=business_pk)
    for quarter in quarter_reports:
        quarters.append(quarter.serialize())
    data = {
        'yearly_reports': years,
        'quarter_reports': quarters,
    }
    return JsonResponse(data)


def get_business_list(request):
    businesses = Business.objects.all()
    result = []
    for business in businesses:
        result.append(business.serialize())
    data = {
        'businesses': result
    }
    return JsonResponse(data)
