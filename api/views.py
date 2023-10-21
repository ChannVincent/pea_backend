from django.shortcuts import render
from core.models.business import Business, BusinessRatio
from django.http import JsonResponse


def get_business_detail(request, business_pk):
    if not business_pk:
        return JsonResponse({'status': 'error : no business found'})
    business = Business.objects.filter(pk=business_pk).first()
    business_ratios = BusinessRatio.objects.filter(business=business).order_by('year').all()
    ratios = []
    for ratio in business_ratios:
        ratios.append(ratio.serialize())
    data = {
        'business': business.serialize(),
        'business_ratios': ratios
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
