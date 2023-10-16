from django.urls import path
from core.views import business, sync

# http://localhost:8000/api/[path]
urlpatterns = [
    path("business/<int:business_pk>/", business.get_business_detail, name="business_detail"),
    path("business/", business.get_business_list, name="business_list"),
    path("", sync.index, name="index"),
]