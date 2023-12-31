import requests
from integration.models import DebugApiLog

# https://rapidapi.com/apidojo/api/yahoo-finance1
class YahooFinanceAPI:

    def __init__(self, api_key, api_host) -> None:
        self.base_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock"
        self.rapid_api_key = api_key
        self.rapid_api_host = api_host
        pass

    def get_headers(self):
        headers = {
            'X-RapidAPI-Key': self.rapid_api_key,
            'X-RapidAPI-Host': self.rapid_api_host,
        }
        return headers
    
    def get_stuff(self, stuff, stock, country):
        params = {
            "symbol":stock,
            "region":country,
        }
        url = f"{self.base_url}/{stuff}"
        response = requests.get(
            url, 
            headers=self.get_headers(), 
            params=params)
        body = response.json()
        debug = DebugApiLog(url=url, data=body, params=params)
        debug.save()
        return body
    
    # CA & bénéfices net
    def get_earnings(self, stock, country):
        return self.get_stuff('get-earnings', stock, country)
    
    # cashflow v2/get-cash-flow
    def get_cashflow(self, stock, country):
        return self.get_stuff('v2/get-cash-flow', stock, country)
    
    # summary
    def get_summary(self, stock, country):
        return self.get_stuff('v2/get-summary', stock, country)
        
    # todo stock/get-recent-updates
    # upgradeDowngradeHistory
    # calendarEvents ?
    def get_updates(self, stock, country):
        return self.get_stuff('get-recent-updates', stock, country)

    # v3/get-historical-data
    def get_market_price(self, stock, country):
        return self.get_stuff('v3/get-historical-data', stock, country)
