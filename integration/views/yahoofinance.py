import requests

class YahooFinanceAPI:

    def __init__(self, api_key, api_host) -> None:
        self.base_url_v1 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock"
        self.base_url_v2 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2"
        self.rapid_api_key = api_key
        self.rapid_api_host = api_host
        pass

    def get_headers(self):
        headers = {
            'X-RapidAPI-Key': self.rapid_api_key,
            'X-RapidAPI-Host': self.rapid_api_host,
        }
        return headers
    
    def get_stuff(self, base_url, stuff, stock, country):
        params = {
            "symbol":stock,
            "region":country,
        }
        response = requests.get(
            f"{base_url}/{stuff}", 
            headers=self.get_headers(), 
            params=params)
        body = response.json()
        return body
    
    # avis analystes
    def get_analysis(self, stock, country):
        return self.get_stuff(self.base_url_v2, 'get-analysis', stock, country)
    
    # financials ?
    def get_financials(self, stock, country):
        return self.get_stuff(self.base_url_v2, 'get-financials', stock, country)
    
    # CA & bénéfices net
    def get_earnings(self, stock, country):
        return self.get_stuff(self.base_url_v1, 'get-earnings', stock, country)