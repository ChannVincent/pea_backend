from core.models.business import Business
from integration.models.alphavantage import AlphavantageIntegration
from integration.views.alphavantage import AlphavantageAPI
import json

def sync_monthly_value():
    alphavantage_integration = AlphavantageIntegration.objects.first()
    alphavantage_api = AlphavantageAPI(alphavantage_integration.base_url, alphavantage_integration.api_key)
    businesses = Business.objects.all()
    for business in businesses:
        symbol = business.symbol
        result = alphavantage_api.get_monthly_value(symbol=symbol)
        print(json.dumps(result))
