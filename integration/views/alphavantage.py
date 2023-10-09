import requests

class AlphavantageAPI:

    def __init__(self, base_url, api_key) -> None:
        self.base_url = base_url
        self.api_key = api_key
        pass

    def get_headers(self):
        headers = {}
        return headers

    def get_monthly_value(self, symbol):
        params = {
            "function": "TIME_SERIES_MONTHLY",
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = requests.get(
            url=self.base_url,
            params=params,
        )
        body = response.json()
        return body