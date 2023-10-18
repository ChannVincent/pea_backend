from django.urls import path
from integration.tasks import yahoofinance

# http://localhost:8000/integration/[path]
urlpatterns = [
    path("sync_business/<int:business_id>/", yahoofinance.sync_business, name="sync_business"),
    path("sync_business/", yahoofinance.sync_businesses, name="sync_businesses"),
]