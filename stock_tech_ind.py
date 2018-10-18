#Libraries
import requests
import stock_historical_data
import datetime

def simple_moving_average(data_set, date, days): #pass raw["Time Series (Daily)"]
    key = '4. close'
    print("SMA CLALED!")
    date_obj = datetime.date(*map(int, date.split("-"))) #build the date_obj
    average = float(data_set[date][key])
    days_past = days - 1
    while days_past != 0:
        date_obj = date_obj - datetime.timedelta(1)
        p_date = date_obj.strftime("%Y-%m-%d")
        if data_set.get(p_date, "ERROR") == 'ERROR': #not a trading day
            pass
        else:
            print(float(data_set[p_date][key]))
            average += float(data_set[p_date][key])
            days_past -= 1

    average /= days

    return average
    
#Main
def main():
    print("Stock Tech Ind Tests")
    raw = stock_historical_data.toJson(stock_historical_data.historical_data("AAPL", outputsize='compact', datatype='json'))
    raw = raw["Time Series (Daily)"]
    print(simple_moving_average(raw, '2018-10-17', 5))

if __name__ == '__main__':
    main()