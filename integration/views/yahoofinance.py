import requests

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
        response = requests.get(
            f"{self.base_url}/{stuff}", 
            headers=self.get_headers(), 
            params=params)
        body = response.json()
        return body
    
    # todo summary v3/get-profile
    # todo avis analystes v2/get-analysis
    # todo financials v2/get-financials
    
    # CA & bénéfices net
    def get_earnings(self, stock, country):
        return self.get_stuff('get-earnings', stock, country)
    
    # cashflow v2/get-cash-flow
    # cash trésorerie
    # cash investie
    # free, invest, operating cashflox
    def get_cashflow(self, stock, country):
        return self.get_stuff('v2/get-cash-flow', stock, country)

