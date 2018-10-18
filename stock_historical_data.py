import requests

_API_KEY = "6GKUV6O2AMQKYYTM"

def toJson(historical_data):
    return historical_data.json()

'''
historical_data
@param company_ticker e.g. AAPL
@param outputsize full or compact
@param datatype csv or json
'''
def historical_data(company_ticker, outputsize="full", datatype="csv"):
    return requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=" + outputsize + "&symbol=" + company_ticker + "&apikey=" + _API_KEY + "&datatype=" + datatype)

def main():
    print("historical data tests")
    
    raw = toJson(historical_data("AAPL", outputsize='compact', datatype='json'))
    print(raw)

    raw = toJson(historical_data("TSLA", outputsize='compact', datatype='json'))
    print(raw)

if __name__ == '__main__':
    main()