import requests
import pandas as pd
import json

#API that contains info on exchange rates and currency names that we will be extracting data from
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=<INSERT YOUR API KEY HERE>"
html_data = requests.get(url).text

json_data = json.loads(html_data)
currency_name, rates = [], []
for i in json_data['rates'].items():
    currency_name.append(i[0])
    rates.append(i[1])

data = pd.DataFrame(rates, columns=['rates'], index=currency_name)
data.to_csv('exchange_rates_1.csv')

