from django.urls import path
from api.views import get_business_detail, get_business_list

# http://localhost:8000/api/[path]
urlpatterns = [
    path("business/<int:business_pk>/", get_business_detail, name="business_detail"),
    path("business/", get_business_list, name="business_list"),
]