from django.urls import path
from core.views import business

# http://localhost:8000/api/[path]
urlpatterns = [
    path("business_detail/<int:business_pk>/", business.get_business_detail, name="business_detail"),
    path("business_list/", business.get_business_list, name="business_list"),
]